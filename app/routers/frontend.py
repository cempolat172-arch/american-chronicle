from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import NewsArticle

router = APIRouter(tags=["frontend"])

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def read_index(request: Request, db: Session = Depends(get_db)):
    """
    Renders the beautiful high-CTR frontend homepage.
    Fetches the latest AI-generated news articles from the database.
    """
    # Fetch latest standard articles
    latest_articles = db.query(NewsArticle).filter(NewsArticle.is_bizarre == False).order_by(NewsArticle.published_at.desc()).limit(12).all()
    
    # Fetch breaking news
    breaking_articles = db.query(NewsArticle).filter(NewsArticle.is_breaking == True).order_by(NewsArticle.published_at.desc()).limit(3).all()
    
    # Fetch bizarre / ultra-interesting news
    bizarre_articles = db.query(NewsArticle).filter(NewsArticle.is_bizarre == True).order_by(NewsArticle.published_at.desc()).limit(4).all()
    return templates.TemplateResponse(
        request,
        "index.html", 
        {
            "articles": latest_articles,
            "breaking": breaking_articles,
            "bizarre": bizarre_articles,
            "category": None
        }
    )

@router.get("/category/{slug}")
def read_category(request: Request, slug: str, db: Session = Depends(get_db)):
    """
    Renders category-specific news by doing simple keyword matching.
    """
    slug_lower = slug.lower()
    
    keyword_map = {
        "yapay-zeka": "AI",
        "siyaset": "politic",
        "sari-basin": "scandal",
        "wild-tech": "tech"
    }
    
    search_term = keyword_map.get(slug_lower, slug_lower)
    
    query = db.query(NewsArticle).filter(
        (NewsArticle.content.ilike(f"%{search_term}%")) | (NewsArticle.title.ilike(f"%{search_term}%"))
    )
    
    latest_articles = query.filter(NewsArticle.is_bizarre == False).order_by(NewsArticle.published_at.desc()).limit(12).all()
    breaking_articles = query.filter(NewsArticle.is_breaking == True).order_by(NewsArticle.published_at.desc()).limit(3).all()
    bizarre_articles = query.filter(NewsArticle.is_bizarre == True).order_by(NewsArticle.published_at.desc()).limit(4).all()
    
    return templates.TemplateResponse(
        request,
        "index.html", 
        {
            "articles": latest_articles,
            "breaking": breaking_articles,
            "bizarre": bizarre_articles,
            "category": slug_lower
        }
    )

@router.get("/search")
def search_articles(request: Request, q: str = "", db: Session = Depends(get_db)):
    """
    Renders search results across all articles matching the query.
    """
    query = db.query(NewsArticle)
    
    if q.strip():
        search_term = q.strip()
        query = query.filter(
            (NewsArticle.content.ilike(f"%{search_term}%")) | (NewsArticle.title.ilike(f"%{search_term}%"))
        )
    
    latest_articles = query.filter(NewsArticle.is_bizarre == False).order_by(NewsArticle.published_at.desc()).limit(20).all()
    breaking_articles = query.filter(NewsArticle.is_breaking == True).order_by(NewsArticle.published_at.desc()).limit(3).all()
    bizarre_articles = query.filter(NewsArticle.is_bizarre == True).order_by(NewsArticle.published_at.desc()).limit(10).all()
    
    return templates.TemplateResponse(
        request,
        "index.html", 
        {
            "articles": latest_articles,
            "breaking": breaking_articles,
            "bizarre": bizarre_articles,
            "category": None,
            "search_query": q
        }
    )

@router.get("/article/{slug}")
def read_article(request: Request, slug: str, db: Session = Depends(get_db)):
    """
    Renders the SEO-optimized article detail view.
    """
    article = db.query(NewsArticle).filter(NewsArticle.slug == slug).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
        
    return templates.TemplateResponse(
        request,
        "article.html", 
        {
            "article": article
        }
    )

@router.get("/legal")
def read_legal(request: Request):
    """
    Renders the dedicated legal disclaimer and takedown policy page.
    """
    return templates.TemplateResponse(request, "legal.html")

@router.post("/api/reactions/{article_id}/{reaction_type}")
def add_reaction(article_id: int, reaction_type: str, db: Session = Depends(get_db)):
    article = db.query(NewsArticle).filter(NewsArticle.id == article_id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
        
    if reaction_type == "shock":
        article.reaction_shock = (article.reaction_shock or 0) + 1
        new_count = article.reaction_shock
    elif reaction_type == "fire":
        article.reaction_fire = (article.reaction_fire or 0) + 1
        new_count = article.reaction_fire
    elif reaction_type == "clown":
        article.reaction_clown = (article.reaction_clown or 0) + 1
        new_count = article.reaction_clown
    else:
        raise HTTPException(status_code=400, detail="Invalid reaction type")
        
    db.commit()
    return {"success": True, "new_count": new_count, "reaction_type": reaction_type}

@router.get("/api/latest-breaking")
def get_latest_breaking(db: Session = Depends(get_db)):
    """
    Returns the most recent breaking news article for browser push notifications.
    """
    latest = db.query(NewsArticle).filter(NewsArticle.is_breaking == True).order_by(NewsArticle.id.desc()).first()
    if latest:
        return {"id": latest.id, "title": latest.title, "slug": latest.slug}
    return {"id": 0}
