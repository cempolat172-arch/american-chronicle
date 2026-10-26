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

MAX_WIDTH = 800
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


async def fill_missing_image():
    """Generate the image for ONE article that doesn't have a stored image yet (newest first)."""
    db = SessionLocal()
    try:
        stored = select(ArticleImage.slug)
        article = (db.query(NewsArticle)
                   .filter(NewsArticle.image_url.isnot(None), ~NewsArticle.slug.in_(stored))
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
