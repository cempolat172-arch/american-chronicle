"""
Cover images: generated once on the server (Pollinations free tier = 1 image per 45 s per IP),
stored in the database and served from /img/<slug>.jpg. Visitors never hit the image API directly,
so they never see "free limit reached" errors.
"""
import io
import logging

import httpx
from sqlalchemy import select

from app.database import SessionLocal
from app.models import ArticleImage, NewsArticle

logger = logging.getLogger(__name__)

try:
    from PIL import Image
except Exception:  # Pillow optional; images are stored as-is without it
    Image = None

MAX_WIDTH = 1200  # Google Discover large previews need >= 1200px wide images
KEEP_DAYS = 60   # stored images older than this are pruned to stay within the free database size
JPEG_QUALITY = 72


def _compress(data: bytes) -> bytes:
    if not Image:
        return data
    try:
        img = Image.open(io.BytesIO(data)).convert("RGB")
        if img.width > MAX_WIDTH:
            img = img.resize((MAX_WIDTH, round(img.height * MAX_WIDTH / img.width)))
        out = io.BytesIO()
        img.save(out, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
        return out.getvalue()
    except Exception as e:
        logger.warning(f"Image compression failed, storing original: {e}")
        return data


def migrate_images_v2():
    """One-time: switch all cover images to 1200x675 and regenerate them (runs once, tracked in app_state)."""
    from sqlalchemy import text
    from app.database import engine
    from app.services import state
    if state.get_float("images_v2_done"):
        return
    try:
        with engine.begin() as conn:
            conn.execute(text("UPDATE news_articles SET image_url = REPLACE(image_url, 'width=800&height=500', "
                              "'width=1200&height=675') WHERE image_url LIKE '%width=800&height=500%'"))
            conn.execute(text("DELETE FROM article_images"))
        state.set_float("images_v2_done", 1.0)
        logger.info("Images v2: switched to 1200x675, images will be regenerated in the background.")
    except Exception as e:
        logger.warning(f"Images v2 migration failed: {e}")


def _prune_old_images(db):
    from datetime import datetime, timedelta, timezone
    cutoff = datetime.now(timezone.utc) - timedelta(days=KEEP_DAYS)
    try:
        deleted = db.query(ArticleImage).filter(ArticleImage.created_at < cutoff).delete(synchronize_session=False)
        if deleted:
            db.commit()
            logger.info(f"Pruned {deleted} cover image(s) older than {KEEP_DAYS} days.")
    except Exception as e:
        db.rollback()
        logger.warning(f"Image pruning failed: {e}")


async def fill_missing_image():
    """Generate the image for ONE article that doesn't have a stored image yet (newest first)."""
    db = SessionLocal()
    try:
        _prune_old_images(db)
        from datetime import datetime, timedelta, timezone
        recent = datetime.now(timezone.utc) - timedelta(days=KEEP_DAYS)
        stored = select(ArticleImage.slug)
        article = (db.query(NewsArticle)
                   .filter(NewsArticle.image_url.isnot(None), ~NewsArticle.slug.in_(stored),
                           NewsArticle.published_at >= recent)
                   .order_by(NewsArticle.published_at.desc()).first())
        if not article:
            return
        async with httpx.AsyncClient(timeout=90.0, follow_redirects=True) as client:
            resp = await client.get(article.image_url)
        ctype = resp.headers.get("content-type", "")
        if resp.status_code != 200 or not ctype.startswith("image/") or len(resp.content) < 2000:
            logger.info(f"Image not ready for {article.slug} (HTTP {resp.status_code}), will retry.")
            return
        db.add(ArticleImage(slug=article.slug, data=_compress(resp.content), content_type="image/jpeg"))
        db.commit()
        logger.info(f"Stored cover image for {article.slug}.")
    except Exception as e:
        db.rollback()
        logger.warning(f"Image generation failed: {e}")
    finally:
        db.close()
