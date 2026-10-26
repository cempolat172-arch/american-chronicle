"""Persistent timers (stored in the database) so restarts/redeploys don't burn the Gemini quota."""
import logging
import time

from app.database import SessionLocal
from app.models import AppState

logger = logging.getLogger(__name__)


def get_float(key: str, default: float = 0.0) -> float:
    db = SessionLocal()
    try:
        row = db.get(AppState, key)
        return float(row.value) if row and row.value else default
    except Exception as e:
        logger.warning(f"state read failed for {key}: {e}")
        return default
    finally:
        db.close()


def set_float(key: str, value: float) -> None:
    db = SessionLocal()
    try:
        row = db.get(AppState, key)
        if row:
            row.value = str(value)
        else:
            db.add(AppState(key=key, value=str(value)))
        db.commit()
    except Exception as e:
        db.rollback()
        logger.warning(f"state write failed for {key}: {e}")
    finally:
        db.close()


def now() -> float:
    return time.time()
