import re
import logging
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models import NewsArticle
from app.services.collector import collect_news
from app.services.ai_processor import process_article_with_ai
from app.database import SessionLocal

logger = logging.getLogger(__name__)

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

    image_url = raw_news.get("image_url")
    if not image_url:
        # Fallback to a fast, reliable, deterministic vintage placeholder
        image_url = f"https://picsum.photos/seed/{slug}/800/600?grayscale"

    new_article = NewsArticle(
        title=title,
        slug=slug,
        content=ai_result.get("content", ""),
        original_url=original_url,
        seo_description=ai_result.get("seo_description", ""),
        is_bizarre=ai_result.get("is_bizarre", False),
        is_breaking=ai_result.get("is_breaking", False),
        published_at=raw_news.get("published"),
        image_url=image_url
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

async def run_news_pipeline() -> dict:
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
                
        # Step 2: Limit batch size to 5 to avoid Vercel timeouts (10s) and Gemini RPM limits (15/min)
        batch = new_articles[:5]
        logger.info(f"Processing a fast batch of {len(batch)} new articles out of {len(new_articles)} pending...")
        
        # Step 3: Process AI generation concurrently
        import asyncio
        async def process_single(raw_news):
            try:
                ai_res = await process_article_with_ai(raw_news)
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
                        
        return {
            "status": "success", 
            "message": f"Successfully published {published_count} new articles.",
            "pending_in_queue": len(new_articles) - len(batch) if len(new_articles) > len(batch) else 0
        }
    finally:
        try:
            db.close()
        except Exception as e:
            logger.error(f"Error closing database session: {e}")
