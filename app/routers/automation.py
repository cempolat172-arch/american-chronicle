import logging
from fastapi import APIRouter, BackgroundTasks, HTTPException, Header, Depends, Response
from typing import Optional
from app.services.publisher import run_news_pipeline
from app.config import settings

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api", tags=["automation"])

# API anahtarı kontrolü (.env veya config üzerinden)
def verify_api_key(x_api_key: Optional[str] = Header(None)):
    if x_api_key != settings.AUTOMATION_API_KEY:
        raise HTTPException(status_code=401, detail="Yetkisiz erişim. Geçersiz API anahtarı.")

@router.api_route("/trigger-news", methods=["GET", "POST"], dependencies=[Depends(verify_api_key)])
async def trigger_news_secure(response: Response, background_tasks: BackgroundTasks, wait: bool = False):
    """
    Manuel Haber Tetikleme Endpoint'i (Korumalı).
    Vercel (Serverless) platformları BackgroundTasks desteklemediği için 
    işlemi 2'li küçük paketler halinde bekleterek yapar (max 3 saniye).
    Kullanım: POST /api/trigger-news -H "x-api-key: kronik-admin-123"
    """
    # Prevent Vercel from caching this endpoint!
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    
    logger.info("Cron trigger received.")
    if not wait:
        # Note: the cron job URL still sends ?sync=true; it is ignored on purpose.
        # Reading sources + writing long articles takes 30-90s; answer the cron job right away.
        background_tasks.add_task(run_news_pipeline)
        return {"status": "accepted", "message": "News pipeline started in background."}
    try:
        result = await run_news_pipeline()
        return {"status": "success", "details": result}
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        raise HTTPException(status_code=500, detail=f"Pipeline execution failed: {str(e)}")

@router.api_route("/automation/run-pipeline", methods=["GET", "POST"])
async def legacy_trigger_pipeline(background_tasks: BackgroundTasks, sync: bool = True):
    # Geriye dönük uyumluluk (Legacy)
    if not sync:
        background_tasks.add_task(run_news_pipeline)
        return {"message": "News collection pipeline started in the background."}
    result = await run_news_pipeline()
    return {"message": "Pipeline completed.", "details": result}

@router.get("/automation/status")
def get_system_status():
    """
    Returns the system automation status.
    """
    key_configured = bool(settings.GEMINI_API_KEY)
    key_prefix = (settings.GEMINI_API_KEY[:6] + "...") if key_configured else "NOT_CONFIGURED"
    return {
        "status": "active",
        "scheduler": "running",
        "gemini_configured": key_configured,
        "key_prefix": key_prefix,
        "database_in_use": __import__("app.database", fromlist=["engine"]).engine.dialect.name,
        "message": "Automation service is active and runs every 5 minutes."
    }
