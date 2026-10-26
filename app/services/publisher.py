import re
import logging
from datetime import datetime, timezone, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models import NewsArticle
from app.services.collector import collect_news
from app.services.ai_processor import process_article_with_ai
from app.database import SessionLocal

logger = logging.getLogger(__name__)

# --- Freshness & duplicate-story control -------------------------------------------
FRESH_HOURS = 6  # only news published in the last 6 hours is processed
_STOPWORDS = set("""a an the and or of to in on at for with from by as is are was were be been it its
this that these those after over into amid says said new news vs his her their they he she
will can could would about how why what who up out off more than not no just""".split())
_RECENT_STORY_SIGNATURES: list = []  # signatures of stories published since the server started


def _title_signature(title: str) -> frozenset:
    """Keyword set of a headline (outlet suffix like ' - CNN' removed)."""
    title = re.sub(r"\s+-\s+[^-]{2,40}$", "", title or "").lower()
    words = re.findall(r"[a-z0-9']+", title)
    return frozenset(w for w in words if len(w) > 2 and w not in _STOPWORDS)


def _is_duplicate_story(sig: frozenset, others, threshold: float = 0.5) -> bool:
    for o in others:
        if not o:
            continue
        overlap = len(sig & o) / max(1, min(len(sig), len(o)))
        if overlap >= threshold:
            return True
    return False


def _remember_story(title: str):
    sig = _title_signature(title)
    if sig:
        _RECENT_STORY_SIGNATURES.append(sig)
        del _RECENT_STORY_SIGNATURES[:-500]


def generate_slug(title: str) -> str:
    """Generates a URL-friendly slug for a given title."""
    try:
        title = title.lower()
        title = re.sub(r'[^a-z0-9\s-]', '', title)
        return re.sub(r'[\s-]+', '-', title).strip('-')
    except Exception as e:
        logger.error(f"Error generating slug for title '{title}': {e}")
        return "fallback-slug"

def check_article_exists(db: Session, original_url: str) -> bool:
    """Checks if an article with the same original_url already exists in the database."""
    try:
        return db.query(NewsArticle).filter(NewsArticle.original_url == original_url).first() is not None
    except SQLAlchemyError as e:
        logger.error(f"Database error while checking if article exists: {e}")
        raise

def publish_article(db: Session, raw_news: dict, ai_result: dict) -> Optional[NewsArticle]:
    """Saves the AI-processed article to the database."""
    original_url = raw_news.get("link")
    
    try:
        if check_article_exists(db, original_url):
            logger.info(f"Article already exists in DB: {original_url}")
            return None
    except Exception as e:
        logger.error(f"Failed to check existence for {original_url}: {e}")
        return None

    title = ai_result.get("title", "Untitled News")
    slug = generate_slug(title)
    
    # Ensure unique slug safely
    try:
        base_slug = slug
        counter = 1
        while db.query(NewsArticle).filter(NewsArticle.slug == slug).first():
            slug = f"{base_slug}-{counter}"
            counter += 1
    except SQLAlchemyError as e:
        logger.error(f"Database error while generating unique slug: {e}")
        return None

    # Priority: 1) AI-generated Pollinations.ai image from ai_result, 2) RSS feed image, 3) picsum fallback
    image_url = ai_result.get("image_url") or raw_news.get("image_url")
    if not image_url:
        # Auto-generate AI image from article title as final fallback
        from app.services.ai_processor import build_ai_image_url
        image_url = build_ai_image_url(title, slug, ai_result.get("is_bizarre", False))

    new_article = NewsArticle(
        title=title,
        slug=slug,
        content=ai_result.get("content", ""),
        original_url=original_url,
        seo_description=ai_result.get("seo_description", ""),
        is_bizarre=ai_result.get("is_bizarre", False),
        is_breaking=ai_result.get("is_breaking", False),
        published_at=raw_news.get("published") or datetime.now(timezone.utc),
        image_url=image_url,
        keywords=ai_result.get("keywords") or None
    )

    try:
        db.add(new_article)
        db.commit()
        db.refresh(new_article)
        logger.info(f"Successfully published: {title}")
        return new_article
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error saving article '{title}': {e}")
        return None
    except Exception as e:
        db.rollback()
        logger.error(f"Unexpected error saving article '{title}': {e}")
        return None

_PIPELINE_LOCK = None


async def run_news_pipeline() -> dict:
    """Runs the pipeline; if a run is already in progress (scheduler + cron trigger), skip."""
    global _PIPELINE_LOCK
    import asyncio
    if _PIPELINE_LOCK is None:
        _PIPELINE_LOCK = asyncio.Lock()
    if _PIPELINE_LOCK.locked():
        logger.info("Pipeline already running, skipping this trigger.")
        return {"status": "skipped", "message": "Pipeline already running."}
    async with _PIPELINE_LOCK:
        return await _run_news_pipeline()


async def _run_news_pipeline() -> dict:
    """Main pipeline to collect, process, and publish news concurrently & quickly."""
    logger.info("Starting optimized news collection pipeline...")
    
    try:
        raw_news_list = await collect_news()
        logger.info(f"Collected {len(raw_news_list)} raw articles.")
    except Exception as e:
        logger.error(f"Failed to collect news: {e}")
        return {"status": "error", "message": "Collection failed"}

    try:
        db = SessionLocal()
    except Exception as e:
        logger.error(f"Failed to create database session: {e}")
        return {"status": "error", "message": "DB connection failed"}
        
    try:
        # Step 1: Filter out existing articles synchronously
        new_articles = []
        for raw_news in raw_news_list:
            original_url = raw_news.get("link")
            if not original_url:
                continue
            if not check_article_exists(db, original_url):
                new_articles.append(raw_news)
                
        # Only keep FRESH news: skip anything older than FRESH_HOURS (old backlog is dropped, not queued)
        cutoff = datetime.now(timezone.utc) - timedelta(hours=FRESH_HOURS)
        fresh = [n for n in new_articles if n.get('published') and n['published'] >= cutoff]
        skipped_old = len(new_articles) - len(fresh)

        # Sort by published date descending (newest first) so the site is always fresh
        fresh.sort(key=lambda x: x['published'], reverse=True)

        # Drop duplicates of the same story coming from different outlets
        new_articles = []
        for n in fresh:
            sig = _title_signature(n.get('title', ''))
            if not sig or _is_duplicate_story(sig, [_title_signature(a.get('title', '')) for a in new_articles]):
                continue
            if _is_duplicate_story(sig, _RECENT_STORY_SIGNATURES):
                continue
            new_articles.append(n)
        logger.info(f"Fresh (<{FRESH_HOURS}h) unique stories: {len(new_articles)} | skipped old: {skipped_old}")
        
        # Step 2: Limit batch size to 5 to avoid Vercel timeouts (10s) and Gemini RPM limits (15/min)
        from app.services.ai_processor import gemini_in_cooldown
        from app.config import settings
        import time
        from app.services import state
        last_ai_run = state.get_float("last_ai_run")
        wait_left = last_ai_run + settings.ARTICLE_INTERVAL_MINUTES * 60 - time.time()
        if wait_left > 0:
            logger.info(f"Next article slot in {int(wait_left // 60)} min (free-tier pacing).")
            return {"status": "waiting", "message": f"Next article in {int(wait_left // 60)} min.", "pending_in_queue": len(new_articles)}
        if gemini_in_cooldown():
            logger.info("Gemini quota cooldown active; skipping AI writing this run.")
            return {"status": "cooldown", "message": "Gemini quota exceeded, waiting.", "pending_in_queue": len(new_articles)}
        # Pick stories whose full text we can actually read (free, no AI quota used).
        # Unreadable ones (paywall, blocked) are skipped instead of wasting an AI request.
        from app.services.article_reader import fetch_source_article
        from app.services.ai_processor import MIN_SOURCE_WORDS
        wanted = max(1, settings.ARTICLES_PER_RUN)
        batch, sources, checked = [], {}, 0
        for candidate in new_articles[:15]:
            if len(batch) >= wanted:
                break
            checked += 1
            src = await fetch_source_article(candidate.get("link", ""))
            if len(src.get("text", "").split()) >= MIN_SOURCE_WORDS:
                batch.append(candidate)
                sources[candidate.get("link")] = src
        logger.info(f"Readable source found for {len(batch)} of {checked} checked stories.")
        if not batch and new_articles:
            # Nothing readable: let the AI research the newest story with Google Search instead
            batch = new_articles[:1]
        if batch:
            state.set_float("last_ai_run", time.time())
        logger.info(f"Processing a safe batch of {len(batch)} new articles to avoid Gemini rate limits...")
        
        # Step 3: Process AI generation concurrently
        import asyncio
        async def process_single(raw_news):
            try:
                ai_res = await process_article_with_ai(raw_news, sources.get(raw_news.get("link")))
                return raw_news, ai_res
            except Exception as e:
                logger.error(f"AI error for {raw_news.get('title')}: {e}")
                return None
                
        tasks = [process_single(news) for news in batch]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Step 4: Save to DB sequentially to avoid transaction locks
        published_count = 0
        for res in results:
            if isinstance(res, tuple):
                raw, ai_res = res
                if ai_res:
                    if publish_article(db, raw, ai_res):
                        published_count += 1
                        _remember_story(raw.get('title', ''))
                        
        return {
            "status": "success", 
            "message": f"Successfully published {published_count} new articles.",
            "pending_in_queue": len(new_articles) - len(batch) if len(new_articles) > len(batch) else 0,
            "skipped_old": skipped_old
        }
    finally:
        try:
            db.close()
        except Exception as e:
            logger.error(f"Error closing database session: {e}")
