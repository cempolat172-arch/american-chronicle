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
    """Main pipeline to collect, process, and publish news."""
    logger.info("Starting news collection pipeline...")
    
    try:
        raw_news_list = await collect_news()
        logger.info(f"Collected {len(raw_news_list)} raw articles.")
    except Exception as e:
        logger.error(f"Failed to collect news: {e}")
        return {"status": "error", "message": f"Failed to collect news: {str(e)}"}

    try:
        db = SessionLocal()
    except Exception as e:
        logger.error(f"Failed to create database session: {e}")
        return {"status": "error", "message": f"Database connection failed: {str(e)}"}
        
    processed_count = 0
    errors = []
    
    try:
        for raw_news in raw_news_list:
            original_url = raw_news.get("link")
            if not original_url:
                logger.warning("Found an article with no link. Skipping.")
                continue

            try:
                # Check duplication before AI processing to save API costs
                if check_article_exists(db, original_url):
                    logger.info(f"Skipping duplicate article: {original_url}")
                    continue

                logger.info(f"Processing with AI: {raw_news.get('title')}")
                ai_result = await process_article_with_ai(raw_news)
                
                if ai_result:
                    published = publish_article(db, raw_news, ai_result)
                    if published:
                        processed_count += 1
                else:
                    logger.warning(f"AI processing returned None for: {original_url}")
                    errors.append({"url": original_url, "error": "AI processing returned None"})
                
                import asyncio
                # Hız limiti (Rate Limit) aşımını önlemek için 5 saniye bekle
                await asyncio.sleep(5)
            except Exception as item_error:
                error_msg = f"Error processing article {original_url}: {str(item_error)}"
                logger.error(error_msg)
                errors.append({"url": original_url, "error": str(item_error)})
                # Continue with the next article instead of crashing the pipeline
                continue
    finally:
        try:
            db.close()
        except Exception as e:
            logger.error(f"Error closing database session: {e}")
    
    logger.info(f"Pipeline completed. Published {processed_count} new articles.")
    return {
        "status": "completed", 
        "collected": len(raw_news_list), 
        "published": processed_count,
        "errors": errors
    }
