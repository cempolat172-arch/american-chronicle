import asyncio
import feedparser
import httpx
from datetime import datetime, timezone
from time import mktime
import logging

logger = logging.getLogger(__name__)

RSS_FEEDS = [
    # US Top Stories
    "https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en",
    
    # Hollywood Skandalları (Only last 24 hours)
    "https://news.google.com/rss/search?q=celebrity+scandal+OR+hollywood+drama+OR+gossip+when:1d&hl=en-US&gl=US&ceid=US:en",
    
    # Astroloji (Only last 24 hours)
    "https://news.google.com/rss/search?q=astrology+OR+zodiac+OR+horoscope+when:1d&hl=en-US&gl=US&ceid=US:en",
    
    # UFO, Tuhaf Olaylar (Only last 24 hours)
    "https://news.google.com/rss/search?q=weird+news+OR+UFO+OR+bizarre+OR+conspiracy+when:1d&hl=en-US&gl=US&ceid=US:en",
    
    # Viral Olaylar (Only last 24 hours)
    "https://news.google.com/rss/search?q=viral+OR+trending+OR+drama+when:1d&hl=en-US&gl=US&ceid=US:en",
    
    # US Sports News (Only last 24 hours)
    "https://news.google.com/rss/search?q=sports+OR+nba+OR+nfl+OR+basketball+OR+football+when:1d&hl=en-US&gl=US&ceid=US:en",
    
    # Automotive, Trending Cars, EVs & NHTSA Recalls (Only last 24 hours)
    "https://news.google.com/rss/search?q=car+recall+OR+NHTSA+OR+electric+vehicle+OR+new+SUV+OR+Tesla+OR+Toyota+OR+Ford+OR+GM+when:1d&hl=en-US&gl=US&ceid=US:en",

    # US Economy, Inflation & Consumer Finance (Only last 24 hours)
    "https://news.google.com/rss/search?q=CPI+inflation+OR+Federal+Reserve+OR+mortgage+rates+OR+US+economy+when:1d&hl=en-US&gl=US&ceid=US:en",

    # World News (Dünya Haberleri)
    "https://news.google.com/rss/headlines/section/topic/WORLD?hl=en-US&gl=US&ceid=US:en",

    # Direct publisher feeds: links point straight to the article, so the full text can be read
    # (Google News links can't be resolved from datacenter IPs).
    "https://feeds.npr.org/1001/rss.xml",
    "https://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml",
    "https://www.theguardian.com/us-news/rss",
    "https://www.cbsnews.com/latest/rss/main",
    "https://feeds.nbcnews.com/nbcnews/public/news",
    "https://abcnews.go.com/abcnews/topstories",
    "https://moxie.foxnews.com/google-publisher/latest.xml",
    "https://www.espn.com/espn/rss/news",
    "https://www.cbssports.com/rss/headlines/",
]

async def fetch_feed(url: str, client: httpx.AsyncClient):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = await client.get(url, headers=headers, timeout=15.0, follow_redirects=True)
        response.raise_for_status()
        # Parse the XML response
        parsed = feedparser.parse(response.text)
        return parsed
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error fetching feed {url}: {e.response.status_code}")
    except httpx.RequestError as e:
        logger.error(f"Network error fetching feed {url}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error fetching feed {url}: {e}")
    return None

# Gambling promos / betting tips: no news value and restricted by Google AdSense policies
BETTING_KEYWORDS = [
    "bonus code", "promo code", "sportsbook", "betmgm", "draftkings", "fanduel", "caesars sportsbook",
    "bet365", "fanatics sportsbook", "parlay", "best bets", "betting", "odds and picks", "odds, picks",
    "picks and odds", "prediction, odds", "predictions", "player props", "first touchdown scorer",
    "anytime touchdown", "spread pick", "over/under pick",
]

SPAM_KEYWORDS = BETTING_KEYWORDS + [
    "stream", "livestream", "watch live", "nfhs", "!+", "√", "☯️", 
    "high school", "varsity", "prep football", "where to watch", 
    "how to watch", "free live", "tv broadcast"
]

def is_spam_entry(title: str, summary: str) -> bool:
    content_lower = f"{title} {summary}".lower()
    for kw in SPAM_KEYWORDS:
        if kw in content_lower:
            return True
    # Filter weird unicode bold/italic alphabets frequently used in spam
    if any(ord(c) > 0x1D400 for c in title):
        return True
    if len(title.strip()) < 15:
        return True
    return False

async def collect_news() -> list[dict]:
    """
    Fetches raw news from predefined RSS feeds AND live US Google Trends asynchronously.
    Returns a list of dictionaries containing title, link, summary, and published date.
    Filters out streaming spam and malformed entries.
    """
    raw_news = []
    import urllib.parse

    # Dynamically build search feeds for today's top live US Google Trends
    trend_feeds: list[tuple[str, str]] = []
    try:
        from app.routers.frontend import get_live_trends
        live_trends = get_live_trends() or []
        for term in live_trends[:6]:
            q = urllib.parse.quote_plus(f"{term} when:1d")
            trend_feeds.append((term, f"https://news.google.com/rss/search?q={q}&hl=en-US&gl=US&ceid=US:en"))
    except Exception as e:
        logger.warning(f"Could not build live Google Trends RSS feeds: {e}")

    try:
        async with httpx.AsyncClient() as client:
            all_urls = [url for _, url in trend_feeds] + list(RSS_FEEDS)
            tasks = [fetch_feed(url, client) for url in all_urls]
            results = await asyncio.gather(*tasks, return_exceptions=True)

            for idx, parsed in enumerate(results):
                is_trend_feed = idx < len(trend_feeds)
                trend_term = trend_feeds[idx][0] if is_trend_feed else None
                if isinstance(parsed, Exception):
                    logger.error(f"Exception raised during feed fetch: {parsed}")
                    continue
                if not parsed or not hasattr(parsed, 'entries'):
                    continue
                
                # Take top 2 stories per live trend feed so we don't flood the queue with one topic
                entries = parsed.entries[:2] if is_trend_feed else parsed.entries
                for entry in entries:
                    try:
                        title = entry.get("title", "").strip()
                        summary = entry.get("summary", "").strip()
                        if is_spam_entry(title, summary):
                            continue
                            
                        published_time = None
                        if hasattr(entry, 'published_parsed') and entry.published_parsed:
                            published_time = datetime.fromtimestamp(mktime(entry.published_parsed), tz=timezone.utc)
                        
                        image_url = None
                        if hasattr(entry, 'media_content') and len(entry.media_content) > 0:
                            image_url = entry.media_content[0].get('url')
                        elif hasattr(entry, 'enclosures') and len(entry.enclosures) > 0:
                            for enc in entry.enclosures:
                                if enc.get('type', '').startswith('image/'):
                                    image_url = enc.get('href')
                                    break
                        if not image_url and '<img ' in summary:
                            import re
                            img_match = re.search(r'<img[^>]+src="([^">]+)"', summary)
                            if img_match:
                                image_url = img_match.group(1)

                        raw_news.append({
                            "title": title,
                            "link": entry.get("link", ""),
                            "summary": summary,
                            "published": published_time,
                            "image_url": image_url,
                            "is_trend": is_trend_feed,
                            "trend_term": trend_term,
                        })
                    except Exception as e:
                        logger.error(f"Error parsing entry {entry.get('link', 'unknown')}: {e}")
                        continue
    except Exception as e:
        logger.error(f"Critical error in collect_news: {e}")
        raise
        
    return raw_news
