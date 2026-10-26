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
        from app.db_sync import sync_bundled_articles
        sync_bundled_articles()
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

from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(frontend.router)
app.include_router(automation.router)
