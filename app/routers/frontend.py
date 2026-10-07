from fastapi import APIRouter, Depends, Request, Response, HTTPException
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
    # Get sidebar specific world articles
    world_conditions = [NewsArticle.content.ilike(f"%{kw}%") for kw in ["world", "global", "international", "nation", "europe", "asia", "middle east", "un", "war", "earthquake", "tsunami", "summit", "crisis"]]
    world_conditions.extend([NewsArticle.title.ilike(f"%{kw}%") for kw in ["world", "global", "international", "nation", "europe", "asia", "middle east", "un", "war", "earthquake", "tsunami", "summit", "crisis"]])
    from sqlalchemy import or_
    world_articles = db.query(NewsArticle).filter(or_(*world_conditions)).order_by(NewsArticle.published_at.desc()).limit(5).all()
    
    return templates.TemplateResponse(
        request,
        "index.html", 
        {
            "articles": latest_articles,
            "breaking": breaking_articles,
            "bizarre": bizarre_articles,
            "world_articles": world_articles,
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
        "ai": ["artificial intelligence", "chatgpt", "openai", "machine learning"],
        "politics": ["politic", "election", "president", "biden", "trump", "senate", "congress", "white house"],
        "tabloids": ["scandal", "hollywood", "celebrity", "gossip", "kardashian", "taylor swift"],
        "tech": ["tech", "apple", "google", "cyber", "elon musk", "software", "startup"],
        "astrology": ["astrology", "zodiac", "horoscope", "retrograde", "tarot", "horoscopes", "zodiac sign", "aries", "taurus", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"],
        "sports": ["sport", "nba", "nfl", "basketball", "football", "baseball", "soccer", "lakers", "lebron", "messi", "ronaldo", "athlete", "championship", "coach"],
        "world": ["world", "global", "international", "nation", "europe", "asia", "middle east", "un", "war", "earthquake", "tsunami", "summit", "crisis"]
    }
    
    keywords = keyword_map.get(slug_lower, [slug_lower])
    
    # Create an OR condition for all keywords in the list
    from sqlalchemy import or_
    conditions = []
    for kw in keywords:
        conditions.append(NewsArticle.content.ilike(f"%{kw}%"))
        conditions.append(NewsArticle.title.ilike(f"%{kw}%"))
        
    query = db.query(NewsArticle).filter(or_(*conditions))
    
    latest_articles = query.filter(NewsArticle.is_bizarre == False).order_by(NewsArticle.published_at.desc()).limit(12).all()
    breaking_articles = query.filter(NewsArticle.is_breaking == True).order_by(NewsArticle.published_at.desc()).limit(3).all()
    bizarre_articles = query.filter(NewsArticle.is_bizarre == True).order_by(NewsArticle.published_at.desc()).limit(4).all()
    
    # Get sidebar specific world articles
    world_conditions = [NewsArticle.content.ilike(f"%{kw}%") for kw in ["world", "global", "international", "nation", "europe", "asia", "middle east", "un", "war", "earthquake", "tsunami", "summit", "crisis"]]
    world_conditions.extend([NewsArticle.title.ilike(f"%{kw}%") for kw in ["world", "global", "international", "nation", "europe", "asia", "middle east", "un", "war", "earthquake", "tsunami", "summit", "crisis"]])
    from sqlalchemy import or_
    world_articles = db.query(NewsArticle).filter(or_(*world_conditions)).order_by(NewsArticle.published_at.desc()).limit(5).all()
    
    return templates.TemplateResponse(
        request,
        "index.html", 
        {
            "articles": latest_articles,
            "breaking": breaking_articles,
            "bizarre": bizarre_articles,
            "world_articles": world_articles,
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
    
    # Get sidebar specific world articles
    world_conditions = [NewsArticle.content.ilike(f"%{kw}%") for kw in ["world", "global", "international", "nation", "europe", "asia", "middle east", "un", "war", "earthquake", "tsunami", "summit", "crisis"]]
    world_conditions.extend([NewsArticle.title.ilike(f"%{kw}%") for kw in ["world", "global", "international", "nation", "europe", "asia", "middle east", "un", "war", "earthquake", "tsunami", "summit", "crisis"]])
    from sqlalchemy import or_
    world_articles = db.query(NewsArticle).filter(or_(*world_conditions)).order_by(NewsArticle.published_at.desc()).limit(5).all()
    
    return templates.TemplateResponse(
        request,
        "index.html", 
        {
            "articles": latest_articles,
            "breaking": breaking_articles,
            "bizarre": bizarre_articles,
            "world_articles": world_articles,
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

@router.get("/play")
def play_game(request: Request):
    """
    Renders the custom HTML5 Canvas Agar.io style game.
    """
    return templates.TemplateResponse(request, "game_agar.html")

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


@router.get("/feed.xml")
def generate_rss_feed(db: Session = Depends(get_db)):
    """
    Generates a standard RSS 2.0 feed required for Google News Publisher Center approval.
    """
    articles = db.query(NewsArticle).order_by(NewsArticle.published_at.desc()).limit(50).all()
    
    base_url = "https://theuschronicle.com"
    
    from email.utils import format_datetime
    from datetime import datetime, timezone
    
    xml_content = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    xml_content += '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">\n'
    xml_content += '  <channel>\n'
    xml_content += '    <title>The American Chronicle</title>\n'
    xml_content += f'    <link>{base_url}</link>\n'
    xml_content += '    <description>The premier digital destination for uncensored, high-impact journalism in the United States.</description>\n'
    xml_content += '    <language>en-us</language>\n'
    xml_content += f'    <atom:link href="{base_url}/feed.xml" rel="self" type="application/rss+xml" />\n'
    
    for article in articles:
        pub_date = article.published_at if article.published_at else datetime.now(timezone.utc)
        rfc2822_date = format_datetime(pub_date)
        
        xml_content += '    <item>\n'
        xml_content += f'      <title>{article.title.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</title>\n'
        xml_content += f'      <link>{base_url}/article/{article.slug}</link>\n'
        xml_content += f'      <guid isPermaLink="true">{base_url}/article/{article.slug}</guid>\n'
        xml_content += f'      <pubDate>{rfc2822_date}</pubDate>\n'
        xml_content += f'      <description>{article.seo_description.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")}</description>\n'
        
        image = article.image_url or f"https://picsum.photos/seed/{article.slug}/800/600?grayscale"
        xml_content += f'      <media:content url="{image}" medium="image" />\n'
        xml_content += '    </item>\n'
        
    xml_content += '  </channel>\n'
    xml_content += '</rss>'
    
    return Response(content=xml_content, media_type="application/rss+xml")

@router.get("/sitemap.xml")
def generate_sitemap(db: Session = Depends(get_db)):
    """
    Generates a dynamic XML sitemap for SEO / Google News discovery.
    """
    # Fetch all articles, ordered by newest first
    articles = db.query(NewsArticle).order_by(NewsArticle.published_at.desc()).all()
    
    # Base URL of the application
    base_url = "https://theuschronicle.com"
    
    # Start XML
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Add Homepage
    xml_content += '  <url>\n'
    xml_content += f'    <loc>{base_url}/</loc>\n'
    xml_content += '    <changefreq>always</changefreq>\n'
    xml_content += '    <priority>1.0</priority>\n'
    xml_content += '  </url>\n'
    
    # Add Categories
    categories = ["ai", "politics", "tabloids", "tech", "astrology", "sports", "world"]
    for cat in categories:
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{base_url}/category/{cat}</loc>\n'
        xml_content += '    <changefreq>hourly</changefreq>\n'
        xml_content += '    <priority>0.8</priority>\n'
        xml_content += '  </url>\n'
    
    # Add Articles
    for article in articles:
        # Some dates might be None
        pub_date = article.published_at.strftime("%Y-%m-%dT%H:%M:%S+00:00") if article.published_at else "2026-01-01T00:00:00+00:00"
        
        xml_content += '  <url>\n'
        xml_content += f'    <loc>{base_url}/article/{article.slug}</loc>\n'
        xml_content += f'    <lastmod>{pub_date}</lastmod>\n'
        xml_content += '    <changefreq>never</changefreq>\n'
        xml_content += '    <priority>0.6</priority>\n'
        xml_content += '  </url>\n'
        
    xml_content += '</urlset>'
    
    return Response(content=xml_content, media_type="application/xml")
