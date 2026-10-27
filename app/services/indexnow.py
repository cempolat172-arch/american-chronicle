"""
IndexNow: tells Bing (and other participating search engines) about new/removed URLs within minutes.
The key file is served at https://theuschronicle.com/<KEY>.txt (see frontend router).
"""
import logging

import httpx

logger = logging.getLogger(__name__)

INDEXNOW_KEY = "7c3e9a51d84f4b2e9f06a1c2b5d8e3f4"
HOST = "theuschronicle.com"
ENDPOINT = "https://api.indexnow.org/indexnow"


def _payload(urls):
    return {"host": HOST, "key": INDEXNOW_KEY, "keyLocation": f"https://{HOST}/{INDEXNOW_KEY}.txt",
            "urlList": list(urls)[:10000]}


def ping(urls) -> None:
    urls = [u for u in urls if u]
    if not urls:
        return
    try:
        with httpx.Client(timeout=10.0) as client:
            r = client.post(ENDPOINT, json=_payload(urls))
        logger.info(f"IndexNow: submitted {len(urls)} URL(s), HTTP {r.status_code}")
    except Exception as e:
        logger.warning(f"IndexNow ping failed: {e}")


async def ping_async(urls) -> None:
    urls = [u for u in urls if u]
    if not urls:
        return
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            r = await client.post(ENDPOINT, json=_payload(urls))
        logger.info(f"IndexNow: submitted {len(urls)} URL(s), HTTP {r.status_code}")
    except Exception as e:
        logger.warning(f"IndexNow ping failed: {e}")


def article_url(slug: str) -> str:
    return f"https://{HOST}/article/{slug}"
