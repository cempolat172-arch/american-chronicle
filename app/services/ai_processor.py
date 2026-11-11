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
        return f"https://image.pollinations.ai/prompt/{encoded}?width=1200&height=675&seed={seed}&nologo=true"
    except Exception as e:
        logger.warning(f"Failed to build AI image URL: {e}")
        return f"https://picsum.photos/seed/{slug}/800/500"


GEMINI_MODEL = "gemini-3-flash-preview"
MIN_SOURCE_WORDS = 150  # below this, Gemini must research the story with Google Search


def _build_prompt(title: str, summary: str, source_url: str, source_text: str, use_search: bool) -> str:
    if use_search or not source_text.strip():
        source_block = f"""Headline: {title}
Publisher link: {source_url}
RSS Summary: {summary}"""
    else:
        source_block = f"""Headline: {title}
Publisher link: {source_url}
RSS Summary: {summary}
SOURCE ARTICLE TEXT:
\"\"\"
{source_text}
\"\"\""""

    return f"""You are a senior investigative news editor and SEO strategist at The American Chronicle, a high-CTR US national news publication.
Read the news dispatch below and write a completely ORIGINAL, comprehensive, deeply engaging, SEO-optimized news article (strictly 650 to 1,000 words).

ACCURACY & CONTEXT RULES:
- Anchor the report in the exact real-world event described in the headline, summary, and source text.
- Never fabricate fake quotes or false scores/numbers. When expanding to 650-1,000 words, add verified institutional, historical, legal, economic, or industry background context, explain why the story matters to American readers, and outline what happens next.
- Do not copy sentences from the source; rewrite completely in your own authoritative journalistic voice to pass 100% plagiarism checks.

SEO & HIGH-CTR RULES:
1. Do keyword research for this story: choose ONE high-volume focus keyword (the exact phrase Americans are typing into Google right now) and 6-8 secondary / long-tail search keywords.
2. title: Generate a high-CTR, punchy, magnetic headline (max 85 characters) with the focus keyword near the start. Use varied journalistic prefixes when fitting (e.g. "BREAKING:", "SHOCKWAVE:", "EXCLUSIVE:", "CRISIS:", "ANALYSIS:") or strong active verbs.
3. content: Markdown article, STRICTLY between 650 and 1,000 words:
   - Start IMMEDIATELY with the opening lead paragraph (do NOT start with a `##` heading on the first line). Answer who/what/when/where with immediate impact and include the **focus keyword** in bold.
   - Second paragraph: highlight the top trending search queries around this topic in **bold**.
   - 4 to 5 engaging `##` (H2) subheadings (and `###` H3 where helpful) containing target search keywords naturally.
   - A 5-item bulleted list (`* **Bold Point:** ...`) summarizing the key takeaways and facts.
   - Deep background context, industry/political implications, and what to watch next.
   - End with a `## Frequently Asked Questions` section: 3 high-intent questions people search on Google, each formatted in **bold** on its own line followed by a clear 2-3 sentence answer.
   - Never include an H1 (`#`) inside `content`.
4. seo_description: Punchy 145-158 character meta description containing the focus keyword, optimized for Google Discover CTR.
5. focus_keyword: the primary focus keyword string.
6. keywords: array of 6-8 secondary keyword strings.
7. is_bizarre: true if the story is weird, viral, entertainment, or offbeat; false otherwise.
8. is_breaking: true if this is an urgent national breaking news development.
9. image_prompt: max 15 words describing a dramatic, photorealistic editorial scene for this story. No people, faces, text, or logos.

Return ONLY valid raw JSON (no ``` fences) with exactly these keys:
"title", "content", "seo_description", "focus_keyword", "keywords", "is_bizarre", "is_breaking", "image_prompt".

{source_block}
"""


# ---------------------------------------------------------------------------------------------
# Model chain: best model first; when its free daily quota is used up, fall back to the next one.
# Free tier (Oct 2026): Flash ~20 req/day, Flash-Lite ~500/day each, Gemma ~14k/day.
# Model names are discovered from the API (ListModels) so new versions are picked up automatically.
# ---------------------------------------------------------------------------------------------
PRIMARY_MODEL = "gemini-3-flash-preview"
SEARCH_MODEL = "gemini-3-flash-preview"
FALLBACK_GUESSES = [
    "gemini-3-flash-preview",
    "gemini-3.5-flash-lite",
    "gemini-flash-lite-latest",
    "gemma-4-31b-it",
]
_models_cache = {"time": 0.0, "names": []}
_model_cooldowns = {}  # model -> epoch seconds until which it is skipped


def _next_quota_reset() -> float:
    """Daily quotas reset at midnight Pacific time."""
    from datetime import datetime, timedelta
    from zoneinfo import ZoneInfo
    now = datetime.now(ZoneInfo("America/Los_Angeles"))
    reset = (now + timedelta(days=1)).replace(hour=0, minute=5, second=0, microsecond=0)
    return reset.timestamp()


def _cooldown_until(model: str) -> float:
    from app.services import state
    return max(_model_cooldowns.get(model, 0.0), state.get_float(f"cooldown:{model}"))


def _set_cooldown(model: str, until: float, reason: str):
    from app.services import state
    import time
    _model_cooldowns[model] = until
    state.set_float(f"cooldown:{model}", until)
    logger.warning(f"Gemini model {model} paused for {int((until - time.time()) // 60)} min ({reason}).")


async def _available_models(api_key: str) -> list:
    import time
    if _models_cache["names"] and time.time() - _models_cache["time"] < 6 * 3600:
        return _models_cache["names"]
    names = []
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.get("https://generativelanguage.googleapis.com/v1beta/models",
                                    params={"pageSize": 1000}, headers={"x-goog-api-key": api_key})
        if resp.status_code == 200:
            for m in resp.json().get("models", []):
                if "generateContent" in m.get("supportedGenerationMethods", []):
                    names.append(m["name"].split("/", 1)[-1])
    except Exception as e:
        logger.warning(f"Could not list Gemini models: {e}")
    if names:
        _models_cache.update(time=time.time(), names=names)
    return names


def _version(name: str) -> float:
    m = re.search(r"-(\d+(?:\.\d+)?)-", name)
    return float(m.group(1)) if m else 0.0


async def _model_chain(api_key: str) -> list:
    names = await _available_models(api_key)
    chain = [PRIMARY_MODEL]
    if names:
        bad = re.compile(r"image|tts|audio|live|vision|embedding|thinking|exp", re.I)
        lite = [n for n in names if re.match(r"gemini-\d+(\.\d+)?-flash-lite", n) and not bad.search(n)]
        # newest version first; for the same version prefer the plain alias over dated snapshots
        lite.sort(key=lambda n: (-_version(n), len(n)))
        seen_versions, lite_pick = set(), []
        for n in lite:
            if _version(n) not in seen_versions:
                seen_versions.add(_version(n))
                lite_pick.append(n)
        gemma = [n for n in names if re.match(r"gemma-\d+-\d+b", n) and not bad.search(n)]
        gemma.sort(key=lambda n: (-int(re.match(r"gemma-(\d+)", n).group(1)),
                                  -int(re.search(r"-(\d+)b", n).group(1))))
        chain += lite_pick[:2] + gemma[:1]
    else:
        chain += FALLBACK_GUESSES
    out = []
    for m in chain:
        if m not in out:
            out.append(m)
    return out


def gemini_in_cooldown() -> bool:
    """True only when every model in the chain is paused (checked cheaply from stored state)."""
    import time
    from app.services import state
    return time.time() < state.get_float("gemini_all_paused_until")


async def _call_model(model: str, prompt: str, api_key: str, use_search: bool = False):
    """Returns (text, status). status: ok | quota | unavailable | error"""
    import time
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    payload = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"temperature": 0.7}}
    if not model.startswith("gemma"):
        payload["generationConfig"]["responseMimeType"] = "application/json"
    try:
        # API key goes in a header (not the URL) so it never appears in server logs
        async with httpx.AsyncClient(timeout=90.0) as http_client:
            resp = await http_client.post(url, json=payload, headers={"x-goog-api-key": api_key})
    except Exception as e:
        logger.warning(f"Gemini call failed ({model}): {e}")
        return None, "error"
    if resp.status_code == 429:
        daily = "PerDay" in resp.text or "per day" in resp.text.lower()
        _set_cooldown(model, _next_quota_reset() if daily else time.time() + 120,
                      "daily quota used up" if daily else "per-minute limit")
        return None, "quota"
    if resp.status_code == 404:
        _set_cooldown(model, time.time() + 3600, f"unavailable, HTTP {resp.status_code}")
        logger.warning(f"{model}: {resp.text[:200]}")
        return None, "unavailable"
    if resp.status_code != 200:
        logger.warning(f"Gemini API status {resp.status_code} ({model}): {resp.text[:300]}")
        return None, "error"
    try:
        parts = resp.json()["candidates"][0]["content"]["parts"]
        return "".join(p.get("text", "") for p in parts), "ok"
    except Exception as e:
        logger.warning(f"Unexpected Gemini response ({model}): {e}")
        return None, "error"


async def _call_gemini(prompt: str, api_key: str, use_search: bool = False) -> Optional[str]:
    import time
    from app.services import state
    chain = await _model_chain(api_key)
    for model in chain:
        if time.time() < _cooldown_until(model):
            continue
        text, status = await _call_model(model, prompt, api_key, False)
        if status == "ok":
            logger.info(f"Article written with {model}.")
            return text
        # quota/unavailable/error -> try the next model in the chain
    soonest = min((_cooldown_until(m) for m in chain), default=0.0)
    if soonest > time.time():
        state.set_float("gemini_all_paused_until", soonest)
        logger.warning(f"All Gemini models paused until {time.strftime('%H:%M UTC', time.gmtime(soonest))}.")
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


async def process_article_with_ai(raw_news: dict, source: Optional[dict] = None) -> Optional[dict]:
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        logger.error("GEMINI CRITICAL ERROR: API key is not configured.")
        return None

    title = raw_news.get("title", "")
    summary = re.sub(r"<[^>]+>", " ", raw_news.get("summary", "")).strip()
    link = raw_news.get("link", "")

    # 1) Read the real article
    if source is None:
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
    # Strip any leading H1/H2 heading on the very first line so the article opens with a strong lead paragraph
    content = re.sub(r"^\s*#{1,3}\s+[^\n]+\n+", "", content).strip()
    if len(content.split()) < 450:
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
        image_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1200&height=675&seed={seed}&nologo=true"
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
