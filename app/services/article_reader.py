"""
Reads the real source article behind a Google News RSS link.

1. Google News RSS links (news.google.com/rss/articles/...) are resolved to the
   publisher's real URL via Google News' own batchexecute endpoint.
2. The publisher page is downloaded and its main text is extracted
   (trafilatura if installed, otherwise a simple <p> extractor).
"""
import html as html_lib
import json
import logging
import re
import urllib.parse
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

try:
    import trafilatura
except Exception:  # library optional
    trafilatura = None

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
MAX_SOURCE_CHARS = 12000


async def decode_google_news_url(url: str, client: httpx.AsyncClient) -> Optional[str]:
    """Turns a news.google.com/rss/articles/<id> link into the publisher URL."""
    if "news.google.com" not in url:
        return url
    match = re.search(r"/articles/([^/?#]+)", url)
    if not match:
        return None
    article_id = match.group(1)
    try:
        page = await client.get(f"https://news.google.com/articles/{article_id}", headers=HEADERS)
        sig = re.search(r'data-n-a-sg="([^"]+)"', page.text)
        ts = re.search(r'data-n-a-ts="([^"]+)"', page.text)
        if not sig or not ts:
            logger.warning("Google News decode: signature not found")
            return None
        inner = (
            '["garturlreq",[["X","X",["X","X"],null,null,1,1,"US:en",null,1,null,null,null,null,null,0,1],'
            f'"X","X",1,[1,1,1],1,1,null,0,0,null,0],"{article_id}",{ts.group(1)},"{sig.group(1)}"]'
        )
        payload = "f.req=" + urllib.parse.quote(json.dumps([[["Fbv4je", inner, None, "generic"]]]))
        resp = await client.post(
            "https://news.google.com/_/DotsSplashUi/data/batchexecute",
            content=payload,
            headers={**HEADERS, "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"},
        )
        body = resp.text.split("\n\n", 1)[1]
        data = json.loads(body)
        decoded = json.loads(data[0][2])[1]
        return decoded if decoded.startswith("http") else None
    except Exception as e:
        logger.warning(f"Google News decode failed: {e}")
        return None


def _simple_extract(page_html: str) -> str:
    page_html = re.sub(r"(?is)<(script|style|noscript|header|footer|nav|aside)[^>]*>.*?</\1>", " ", page_html)
    paragraphs = re.findall(r"(?is)<p[^>]*>(.*?)</p>", page_html)
    texts = []
    for p in paragraphs:
        t = html_lib.unescape(re.sub(r"<[^>]+>", "", p)).strip()
        if len(t.split()) >= 8:
            texts.append(t)
    return "\n\n".join(texts)


async def fetch_source_article(google_news_url: str) -> dict:
    """Returns {"url": publisher_url or None, "text": article text ('' if unavailable)}."""
    result = {"url": None, "text": ""}
    try:
        async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as client:
            real_url = await decode_google_news_url(google_news_url, client)
            if not real_url:
                return result
            result["url"] = real_url
            resp = await client.get(real_url, headers=HEADERS)
            if resp.status_code != 200 or "html" not in resp.headers.get("content-type", ""):
                logger.info(f"Source page not readable ({resp.status_code}): {real_url}")
                return result
            text = ""
            if trafilatura:
                text = trafilatura.extract(resp.text, include_comments=False, include_tables=False) or ""
            if len(text.split()) < 120:
                fallback = _simple_extract(resp.text)
                if len(fallback.split()) > len(text.split()):
                    text = fallback
            result["text"] = text[:MAX_SOURCE_CHARS]
    except Exception as e:
        logger.warning(f"Source article fetch failed: {e}")
    return result
