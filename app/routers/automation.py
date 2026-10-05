import logging
from fastapi import APIRouter, BackgroundTasks, HTTPException, Header, Depends
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
async def trigger_news_secure(background_tasks: BackgroundTasks):
    """
    Manuel Haber Tetikleme Endpoint'i (Korumalı).
    Cron-job veya manuel istekler için kullanılır. Cron timeout'larına (30s) takılmamak 
    için işlemi anında arka plana (BackgroundTasks) atar ve anında 200 OK döner.
    Kullanım: POST /api/trigger-news -H "x-api-key: kronik-admin-123"
    """
    logger.info("Cron trigger received. Offloading to background task.")
    background_tasks.add_task(run_news_pipeline)
    return {
        "status": "success",
        "message": "Haber akışı arka planda asenkron olarak başlatıldı. İşlem kısa süre içinde tamamlanacaktır."
    }

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
    return {
        "status": "active",
        "scheduler": "running",
        "message": "Automation service is active and runs every 5 minutes."
    }
