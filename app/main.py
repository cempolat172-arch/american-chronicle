import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.exc import OperationalError
from app.routers import automation, frontend
from app.database import engine, Base
from app.services.publisher import run_news_pipeline

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
# httpx logs full request URLs at INFO level; keep it quiet
logging.getLogger("httpx").setLevel(logging.WARNING)

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Attempt to create tables safely
    try:
        logger.info("Attempting to connect to the database and create tables...")
        Base.metadata.create_all(bind=engine)
        # Lightweight migration: add 'keywords' column to existing databases
        from sqlalchemy import inspect, text
        cols = [c["name"] for c in inspect(engine).get_columns("news_articles")]
        if "keywords" not in cols:
            with engine.begin() as conn:
                conn.execute(text("ALTER TABLE news_articles ADD COLUMN keywords VARCHAR"))
            logger.info("Added 'keywords' column to news_articles.")
        # Copy articles from the bundled news.db into Supabase (only ones not there yet)
        from app.db_sync import sync_bundled_articles, remove_unwanted_articles
        sync_bundled_articles()
        remove_unwanted_articles()
        from app.services.images import migrate_images_v2
        migrate_images_v2()
        logger.info("Database tables verified/created successfully.")
    except OperationalError as e:
        logger.error(f"Failed to connect to the database on startup: {e}")
        logger.warning("Please ensure the database is running and credentials are correct.")
    except Exception as e:
        logger.error(f"Unexpected error during database initialization: {e}")

    # Add and start the APScheduler job
    try:
        scheduler.add_job(
            run_news_pipeline, 
            'interval', 
            minutes=5, 
            id='news_pipeline_job', 
            replace_existing=True
        )
        from app.services.images import fill_missing_image
        # 1 image per minute stays under the image API's free limit (1 per 45 s)
        scheduler.add_job(fill_missing_image, 'interval', seconds=60, id='image_job', replace_existing=True)

        async def _keep_render_awake():
            """Pings external production URL every 8 minutes so Render never spins down the instance."""
            import httpx
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    await client.get("https://theuschronicle.com/api/automation/status")
            except Exception:
                pass

        scheduler.add_job(_keep_render_awake, 'interval', minutes=8, id='keepalive_job', replace_existing=True)
        scheduler.start()
        logger.info("APScheduler started. News pipeline will run every 5 minutes.")
    except Exception as e:
        logger.error(f"Failed to start APScheduler: {e}")
        
    yield
    
    # Shutdown: Stop the scheduler
    try:
        scheduler.shutdown()
        logger.info("APScheduler stopped.")
    except Exception as e:
        logger.error(f"Error shutting down APScheduler: {e}")

app = FastAPI(title="AI Autonomous Tech News Portal", lifespan=lifespan)

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

class HeadMethodMiddleware(BaseHTTPMiddleware):
    """Allows HTTP HEAD requests across all GET routes without 405 Method Not Allowed, essential for search engine bots & crawlers."""
    async def dispatch(self, request, call_next):
        if request.method == "HEAD":
            request.scope["method"] = "GET"
            resp = await call_next(request)
            return Response(content=b"", status_code=resp.status_code, headers=dict(resp.headers), media_type=resp.media_type)
        return await call_next(request)

app.add_middleware(HeadMethodMiddleware)

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(frontend.router)
app.include_router(automation.router)
