import json
import logging
import asyncio
import httpx
from typing import Optional
from app.config import settings

logger = logging.getLogger(__name__)

# Try to import modern google-genai Client safely
try:
    from google import genai
    client = genai.Client(api_key=settings.GEMINI_API_KEY) if settings.GEMINI_API_KEY else None
except Exception:
    client = None

async def process_article_with_ai(raw_news: dict) -> Optional[dict]:
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        logger.error("GEMINI CRITICAL ERROR: API key is not configured.")
        return None

    title = raw_news.get("title", "")
    summary = raw_news.get("summary", "")
    link = raw_news.get("link", "")

    prompt = f"""
You are an expert sensationalist journalist for a viral US-focused "Page 3" tabloid portal.
Your task is to rewrite this news article to be 100% unique (to pass SEO plagiarism checks) and highly engaging for an American audience.
This might be politics, celebrity gossip, crime, bizarre local US news, or tech.

CRITICAL ETHICAL & LEGAL GUARDRAILS:
While you must use a highly dramatic, satirical, and tabloid tone, you MUST NEVER generate direct hate speech, dangerous incitement, or malicious, defamatory attacks against real individuals. Focus the satire on political absurdities, institutional flaws, and general entertainment. Avoid dangerous personal legal violations at all costs.

Requirements:
1. title: Generate an explosive, high-CTR, clickbaity title (max 90 chars). MUST be in English. IMPORTANT: Vary your headline styles wildly! Do NOT use the same prefix for every news. Use diverse styles like "BREAKING:", "EXCLUSIVE:", "ANALYSIS:", "SCANDAL:", "IN-DEPTH:", "SHOCKING:", or just natural newspaper headlines without any prefix. Make them sound like a real, diverse national newspaper.
2. content: ABSOLUTELY MANDATORY: Write HIGHLY DETAILED, comprehensive, and captivating Markdown content with a STRICT MINIMUM OF 500 WORDS (aim for 500-700 words). Do NOT write short summaries! Expand the narrative by adding deep background context, hypothetical implications, expert-style commentary, and dramatic storytelling to increase reader dwell time. NEVER repeat boilerplate legal phrases like 'Our legal team advised us'. Be unique in every single article. Structure the article beautifully with multiple engaging H2 subheadings, bullet points, and bold text for maximum scannability. Spin the narrative completely to ensure zero plagiarism. Crucially, analyze the core topic and organically weave in high-volume, current trending Google Search keywords. Make the article highly discoverable for today's search trends. (in English)
3. seo_description: Punchy SEO meta description (max 160 chars) optimized for Google Discover. (in English)
4. is_bizarre: Boolean. Set to true if the story is genuinely weird, scandalous, mind-blowing, or a crazy crime/celebrity story.
5. is_breaking: Boolean. Set to true if this is an urgent, time-sensitive national US breaking news event.
6. Output Format: Return valid JSON with exactly these keys: "title", "content", "seo_description", "is_bizarre", "is_breaking".
Do NOT include any markdown block formatting like ```json, just return the raw JSON string.

Raw News Information:
Title: {title}
Original Link: {link}
Summary: {summary}
"""

    content_text = None

    # Method 1: Direct Async HTTP REST Call (Fast, Reliable & Model Compatible)
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseMimeType": "application/json"
            }
        }
        async with httpx.AsyncClient(timeout=30.0) as http_client:
            resp = await http_client.post(url, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                content_text = data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                logger.warning(f"REST Gemini API returned status {resp.status_code}: {resp.text[:200]}")
    except Exception as http_err:
        logger.warning(f"REST Gemini call failed, trying SDK fallback: {http_err}")

    # Method 2: SDK Fallback
    if not content_text and client:
        try:
            response = await asyncio.to_thread(
                client.models.generate_content,
                model='gemini-3-flash-preview',
                contents=prompt,
            )
            content_text = response.text
        except Exception as sdk_err:
            logger.warning(f"SDK Gemini call failed: {sdk_err}")

    if not content_text:
        logger.warning(f"All Gemini generation attempts failed for '{title}'.")
        return None

    try:
        cleaned_text = content_text.strip()
        if cleaned_text.startswith("```json"):
            cleaned_text = cleaned_text[7:]
        elif cleaned_text.startswith("```"):
            cleaned_text = cleaned_text[3:]
            
        if cleaned_text.endswith("```"):
            cleaned_text = cleaned_text[:-3]
            
        cleaned_text = cleaned_text.strip()
        
        result = json.loads(cleaned_text)
        return {
            "title": result.get("title", "Untitled News"),
            "content": result.get("content", ""),
            "seo_description": result.get("seo_description", ""),
            "is_bizarre": bool(result.get("is_bizarre", False)),
            "is_breaking": bool(result.get("is_breaking", False))
        }
    except Exception as e:
        error_msg = str(e).lower()
        logger.warning(f"JSON Parsing Error for AI result ('{title}'): {error_msg}")
        return None
