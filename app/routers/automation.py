import logging
from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.services.publisher import run_news_pipeline

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/automation", tags=["automation"])

@router.api_route("/run-pipeline", methods=["GET", "POST"])
async def trigger_pipeline(sync: bool = True, background_tasks: BackgroundTasks = None):
    """
    Triggers the news pipeline.
    If sync=true, it runs synchronously and returns the result/errors in JSON.
    If sync=false, it runs in the background.
    """
    if not sync:
        if background_tasks:
            background_tasks.add_task(run_news_pipeline)
            return {"message": "News collection pipeline started in the background."}
        else:
            raise HTTPException(status_code=400, detail="Background tasks not available.")

    try:
        logger.info("Manual synchronous pipeline trigger started.")
        result = await run_news_pipeline()
        return {"message": "Pipeline completed.", "details": result}
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        raise HTTPException(status_code=500, detail=f"Pipeline execution failed: {str(e)}")

@router.get("/status")
def get_system_status():
    """
    Returns the system automation status.
    """
    return {
        "status": "active",
        "scheduler": "running",
        "message": "Automation service is active and runs every 2 hours."
    }
