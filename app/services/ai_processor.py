import json
import logging
import asyncio
import re
import urllib.parse
import httpx
from typing import Optional
from app.config import settings
from app.services.article_reader import fetch_source_article

logger = logging.getLogger(__name__)

# Try to import modern google-genai Client safely
try:
    from google import genai
    client = genai.Client(api_key=settings.GEMINI_API_KEY) if settings.GEMINI_API_KEY else None
except Exception:
    client = None


def generate_image_prompt(title: str, is_bizarre: bool = False) -> str:
    """
    Generates a clean, photorealistic image prompt for Pollinations.ai
    based on the article title and category.
    No faces, no text, no logos — pure editorial photography style.
    """
    title_lower = title.lower()

    # Category detection → tailored visual prompt
    if any(w in title_lower for w in ["world series", "baseball", "mlb", "brewers", "rays", "dodgers"]):
        prompt = "cinematic baseball stadium night game dramatic lighting empty field crowd cheering"
    elif any(w in title_lower for w in ["election", "voting", "ballot", "midterm", "senate", "congress"]):
        prompt = "american flag patriotic voting booth ballot box dramatic studio lighting"
    elif any(w in title_lower for w in ["football", "nfl", "college football", "quarterback", "touchdown"]):
        prompt = "american football stadium aerial view night game dramatic floodlights"
    elif any(w in title_lower for w in ["hurricane", "storm", "tornado", "flood", "disaster", "wildfire", "fire"]):
        prompt = "dramatic storm clouds dark sky lightning bolt cinematic weather photography"
    elif any(w in title_lower for w in ["ai", "artificial intelligence", "nuclear", "reactor", "tech", "data center", "gemini"]):
        prompt = "futuristic server room glowing blue neon light technology datacenter cinematic"
    elif any(w in title_lower for w in ["trump", "biden", "president", "white house", "congress", "senate", "political"]):
        prompt = "washington dc capitol building dramatic sunset golden hour american flag"
    elif any(w in title_lower for w in ["stock", "economy", "bitcoin", "market", "wall street", "crypto"]):
        prompt = "stock market trading floor dramatic financial graphs charts golden light"
    elif any(w in title_lower for w in ["halloween", "horror", "scary", "terrifier", "smile", "clown"]):
        prompt = "dark gothic halloween night jack o lanterns eerie orange fog cinematic"
    elif any(w in title_lower for w in ["celebrity", "hollywood", "actor", "actress", "scandal", "gossip"]):
        prompt = "hollywood walk of fame night neon lights glamour cinematic dramatic"
    elif any(w in title_lower for w in ["daylight saving", "clock", "time", "sunshine"]):
        prompt = "vintage analog clock golden hour warm sunlight morning fog cinematic"
    elif any(w in title_lower for w in ["russia", "ukraine", "war", "military", "sanctions"]):
        prompt = "dramatic geopolitical tension map globe world conflict cinematic dark moody"
    elif any(w in title_lower for w in ["immigration", "visa", "border", "green card"]):
        prompt = "american eagle flag freedom immigration liberty dramatic light rays"
    elif any(w in title_lower for w in ["nba", "basketball", "nfl", "sports", "game"]):
        prompt = "empty sports arena dramatic lighting basketball court cinematic photography"
    elif is_bizarre:
        prompt = "surreal bizarre dark dramatic cinematic photography mysterious shadows"
    else:
        prompt = "dramatic american newspaper journalism editorial bold cinematic photography news"

    # Append universal quality enhancers
    prompt += ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
    return prompt


def build_ai_image_url(title: str, slug: str, is_bizarre: bool = False) -> str:
    """
    Builds a Pollinations.ai URL that generates an AI image on-the-fly.
    Uses the article title for a relevant, unique image every time.
    Falls back to picsum for reliability.
    """
    try:
        prompt = generate_image_prompt(title, is_bizarre)
        encoded = urllib.parse.quote(prompt)
        # seed from slug hash ensures same article always gets same image
        seed = abs(hash(slug)) % 999999
        return f"https://image.pollinations.ai/prompt/{encoded}?width=800&height=500&seed={seed}&nologo=true"
    except Exception as e:
        logger.warning(f"Failed to build AI image URL: {e}")
        return f"https://picsum.photos/seed/{slug}/800/500"


GEMINI_MODEL = "gemini-3-flash-preview"
MIN_SOURCE_WORDS = 150  # below this, Gemini must research the story with Google Search


def _build_prompt(title: str, summary: str, source_url: str, source_text: str, use_search: bool) -> str:
    if use_search:
        source_block = f"""The full article text could not be downloaded. Use Google Search to find and read
reporting about THIS exact story from reputable outlets before writing.
Headline: {title}
Publisher link: {source_url}
RSS summary: {summary}"""
    else:
        source_block = f"""Headline: {title}
Publisher link: {source_url}
SOURCE ARTICLE TEXT:
\"\"\"
{source_text}
\"\"\""""

    return f"""You are a senior news reporter and SEO editor at The American Chronicle, a US national news site.
Read the source reporting below and write a completely ORIGINAL news article about the same story.

ACCURACY RULES (most important):
- Use ONLY facts found in the source reporting: names, numbers, dates, places, scores, quotes.
- Never invent quotes, statistics, experts, sources, reactions, or events. No speculation presented as fact.
- If something is unknown, do not guess. A shorter accurate article is better than a padded one.
- You may quote at most two short direct quotes, attributed exactly as in the source.

ORIGINALITY RULES:
- Do not copy sentences or paragraph structure from the source. Rewrite everything in your own words,
  with your own angle, structure, and headings, so it passes plagiarism checks.
- Do not mention or name the source outlet's article as "the source"; write as our own reporting.

SEO RULES:
1. Do keyword research for this story: choose ONE focus keyword (the phrase most Americans would type into
   Google to find this story right now) and 5-8 secondary / long-tail keywords (names, places, "what happened",
   "when is", "how to" style queries people actually search).
2. title: a compelling, accurate news headline, max 70 characters, focus keyword near the start.
   No misleading clickbait. Avoid ALL-CAPS words except short prefixes like "BREAKING:" when truly breaking.
3. content: Markdown article, 700-1200 words depending on how much real information exists.
   - First paragraph: answer who/what/when/where in 2-3 sentences and include the focus keyword.
   - 3-5 H2 (##) subheadings, most containing a keyword naturally; H3 where helpful.
   - Short paragraphs, a bullet list of key facts, **bold** the most important names/terms (not whole sentences).
   - Use secondary keywords naturally; never keyword-stuff.
   - Include background/context ONLY from facts in the source reporting.
   - End with a "## Frequently Asked Questions" section: 3 questions people search, each answered
     in 1-3 sentences using only facts from the source. Format each question in **bold** on its own line.
   - Do not put the headline (H1) inside content.
4. seo_description: 140-155 characters, includes the focus keyword, makes people want to click.
5. focus_keyword: the focus keyword string.
6. keywords: array of 5-8 secondary keyword strings.
7. is_bizarre: true only if the story is genuinely weird/unusual.
8. is_breaking: true only for urgent, nationally significant breaking news from the last few hours.
9. image_prompt: max 15 words describing an editorial photo for the story. No people, faces, text or logos.

Return ONLY raw JSON (no ``` fences) with exactly these keys:
"title", "content", "seo_description", "focus_keyword", "keywords", "is_bizarre", "is_breaking", "image_prompt".

{source_block}
"""


_QUOTA_COOLDOWN_UNTIL = 0.0  # epoch seconds; while in the future, Gemini is not called
QUOTA_COOLDOWN_SECONDS = 30 * 60


def gemini_in_cooldown() -> bool:
    import time
    return time.time() < _QUOTA_COOLDOWN_UNTIL


async def _call_gemini(prompt: str, api_key: str, use_search: bool) -> Optional[str]:
    global _QUOTA_COOLDOWN_UNTIL
    import time
    if gemini_in_cooldown():
        return None
    # API key goes in a header (not the URL) so it never appears in server logs
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"
    payload = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.7}}
    if use_search:
        payload["tools"] = [{"google_search": {}}]
    else:
        payload["generationConfig"]["responseMimeType"] = "application/json"
    try:
        async with httpx.AsyncClient(timeout=120.0) as http_client:
            resp = await http_client.post(url, json=payload, headers={"x-goog-api-key": api_key})
        if resp.status_code == 429:
            _QUOTA_COOLDOWN_UNTIL = time.time() + QUOTA_COOLDOWN_SECONDS
            logger.warning("Gemini quota exceeded (429). Pausing AI writing for 30 minutes.")
            return None
        if resp.status_code != 200:
            logger.warning(f"Gemini API status {resp.status_code}: {resp.text[:300]}")
            return None
        parts = resp.json()["candidates"][0]["content"]["parts"]
        return "".join(p.get("text", "") for p in parts)
    except Exception as e:
        logger.warning(f"Gemini call failed: {e}")
        return None


def _parse_json(text: str) -> Optional[dict]:
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        return json.loads(cleaned)
    except Exception:
        match = re.search(r"\{.*\}", cleaned, re.S)
        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                pass
    return None


async def process_article_with_ai(raw_news: dict) -> Optional[dict]:
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        logger.error("GEMINI CRITICAL ERROR: API key is not configured.")
        return None

    title = raw_news.get("title", "")
    summary = re.sub(r"<[^>]+>", " ", raw_news.get("summary", "")).strip()
    link = raw_news.get("link", "")

    # 1) Read the real article
    source = await fetch_source_article(link)
    source_text = source.get("text", "")
    source_url = source.get("url") or link
    word_count = len(source_text.split())
    use_search = word_count < MIN_SOURCE_WORDS
    logger.info(f"Source for '{title[:60]}': {word_count} words ({'google search' if use_search else 'article text'})")

    # 2) Write an original article from it
    prompt = _build_prompt(title, summary, source_url, source_text, use_search)
    content_text = await _call_gemini(prompt, api_key, use_search)
    if not content_text:
        return None

    result = _parse_json(content_text)
    if not result or not result.get("content"):
        logger.warning(f"Could not parse Gemini JSON for '{title}'")
        return None

    content = result.get("content", "").strip()
    if len(content.split()) < 350:
        logger.warning(f"Article too short ({len(content.split())} words), skipped: '{title}'")
        return None

    ai_title = (result.get("title") or title).strip()
    is_bizarre = bool(result.get("is_bizarre", False))
    keywords = result.get("keywords") or []
    if isinstance(keywords, str):
        keywords = [k.strip() for k in keywords.split(",")]
    focus = (result.get("focus_keyword") or "").strip()
    all_keywords = [k for k in ([focus] + [str(k).strip() for k in keywords]) if k]
    seen = set()
    all_keywords = [k for k in all_keywords if not (k.lower() in seen or seen.add(k.lower()))][:9]

    image_prompt_text = (result.get("image_prompt") or "").strip()
    slug_temp = re.sub(r"[\s-]+", "-", re.sub(r"[^a-z0-9\s-]", "", ai_title.lower())).strip("-")
    if len(image_prompt_text) > 5:
        encoded = urllib.parse.quote(
            image_prompt_text + ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
        )
        seed = abs(hash(slug_temp)) % 999999
        image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=800&height=500&seed={seed}&nologo=true"
    else:
        image_url = build_ai_image_url(ai_title, slug_temp, is_bizarre)

    return {
        "title": ai_title,
        "content": content,
        "seo_description": (result.get("seo_description") or "").strip()[:160],
        "keywords": ", ".join(all_keywords),
        "is_bizarre": is_bizarre,
        "is_breaking": bool(result.get("is_breaking", False)),
        "image_url": image_url,
    }
