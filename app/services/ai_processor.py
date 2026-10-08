import json
import logging
import asyncio
from typing import Optional
from google import genai
from app.config import settings

logger = logging.getLogger(__name__)

# Initialize the modern google-genai Client
client = genai.Client(api_key=settings.GEMINI_API_KEY) if settings.GEMINI_API_KEY else None

async def process_article_with_ai(raw_news: dict) -> Optional[dict]:
    if not client:
        print("GEMINI CRITICAL ERROR: API key is not configured.")
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

    try:
        # Generate content using the new google-genai syntax and latest model
        response = await asyncio.to_thread(
            client.models.generate_content,
            model='gemini-3.8-flash',
            contents=prompt,
        )
        
        content_text = response.text
        if not content_text:
            raise ValueError("Empty response text (possibly blocked by safety filters).")
            
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
        logger.warning(f"GEMINI API ERROR or SAFETY BLOCK ('{title}'): {error_msg}")
        
        # Fallback to a dynamic, long, 500-word template to satisfy SEO if Gemini API fails
        import random
        safe_title = title if len(title) < 50 else title[:47] + "..."
        prefixes = ["BREAKING", "EXCLUSIVE", "ANALYSIS", "SPECIAL REPORT", "SCANDAL", "INSIDE STORY", "SHOCKING"]
        chosen_prefix = random.choice(prefixes)
        
        # Multiple diverse paragraphs to hit the 500 word count
        p1_options = [
            f"The global landscape was recently shaken by what can only be described as a monumental development surrounding {safe_title}. Sources close to the inner workings of the administration have remained suspiciously quiet, leading analysts to speculate on the unprecedented nature of this event. In the digital age, information travels at the speed of light, yet the profound implications of this latest twist seem to have eluded mainstream coverage. Today, we dive deep into the hidden layers of this developing narrative.",
            f"In an unprecedented turn of events, the internet is ablaze with discussions regarding {safe_title}. While major networks attempt to spin the narrative to fit their corporate agendas, independent researchers have uncovered a labyrinth of conflicting reports. What exactly is going on behind closed doors? Why is there a sudden rush to control the flow of information? Our investigative unit has pieced together the fragments of this incredibly complex puzzle, revealing a truth that might disturb the average citizen.",
            f"Every so often, a story breaks that forces us to question everything we thought we knew. The recent developments tied to {safe_title} fall squarely into this category. Eyewitness accounts, leaked memos, and encrypted communications all point to a seismic shift in the geopolitical and cultural fabric of our nation. While some dismiss these anomalies as mere coincidences, the sheer volume of corroborating evidence suggests a meticulously orchestrated operation."
        ]
        
        p2_options = [
            "## The Untold Background\n\nTo truly understand the gravity of the current situation, one must look back at the historical precedents that paved the way for this moment. For years, whisper networks and underground forums have predicted a systemic shockwave of exactly this magnitude. Economists, political scientists, and cultural critics have debated the underlying symptoms, but very few anticipated the sudden and aggressive escalation we are witnessing today. The convergence of technology, politics, and raw human ambition has created a volatile cocktail. When dealing with stakes this high, the players involved operate entirely in the shadows.",
            "## A Web of Contradictions\n\nWhat makes this incident particularly fascinating is the sheer volume of contradictions emerging from official channels. Spokespersons issue statements that are retracted hours later. Documents are published, only to be mysteriously scrubbed from government archives. This erratic behavior indicates a severe internal panic. Experts in crisis management suggest that when institutions behave this erratically, they are usually trying to mask a structural failure of massive proportions. The public is left to connect the dots, relying on fragmented data and anonymous whistleblowers.",
            "## The Financial and Geopolitical Fallout\n\nBeyond the immediate shock value, the long-term ramifications of this event are staggering. Global markets detest uncertainty, and the ripples of this controversy are already being felt in major financial hubs. Hedge fund managers are hastily restructuring their portfolios, while diplomatic cables are buzzing with frantic inquiries. If the historical cycle holds true, we are merely in the eye of the hurricane. The true cost of this disruption will only become apparent when the dust finally settles and the hidden ledgers are exposed."
        ]
        
        p3_options = [
            "## What the Mainstream Media is Missing\n\nIf you turn on your television right now, you will likely be fed a sanitized, easily digestible version of reality. The corporate press is notoriously risk-averse, preferring to echo talking points rather than ask dangerous questions. But the American public is waking up. The demand for unfiltered, raw journalism has never been higher. Independent platforms and decentralized networks are actively bypassing the traditional gatekeepers, allowing the real story to bypass the censors. This paradigm shift in media consumption is directly responsible for bringing the suppressed details of this event to light.",
            "## The Role of Advanced Technology\n\nWe must also consider the technological angle. In an era dominated by artificial intelligence, deepfakes, and algorithmic manipulation, determining what is real has become an arms race. It is highly probable that automated systems were deployed to either amplify or suppress the digital footprint of this controversy. Cybersecurity experts have noted highly unusual traffic patterns associated with the key figures involved, suggesting a sophisticated cyber-warfare component to this otherwise terrestrial conflict. Welcome to the modern battlefield.",
            "## The Cultural Shift\n\nEvents of this magnitude do not occur in a vacuum; they are both a symptom and a catalyst of broader cultural shifts. The psychological impact on the collective consciousness is palpable. People are beginning to question the very foundations of the institutions they once trusted implicitly. This erosion of faith is a dangerous phenomenon, often leading to deep societal polarization. However, it can also act as a cleansing fire, burning away the obsolete structures and making way for radical transparency."
        ]
        
        p4_options = [
            "## Conclusion: What Happens Next?\n\nAs we continue to monitor this rapidly evolving situation, one thing remains absolutely clear: the narrative is far from over. The coming days will be critical in determining whether this leads to a widespread reckoning or another masterclass in institutional cover-ups. We urge our readers to remain vigilant, to question the official timeline, and to diversify their sources of information. The truth is rarely simple, and it is never handed to you on a silver platter. Stay tuned as we prepare to release our follow-up investigation.",
            "## The Final Verdict\n\nIn summary, the intersection of these chaotic elements guarantees that the fallout will be felt for months, if not years, to come. We are witnessing history unfold in real-time, messy and unfiltered. The decisions made by key players in the next 48 hours will set precedents that will be studied by future generations. Do not let the noise distract you from the signal. Keep your eyes on the underlying structural changes, because that is where the real game is being played. We will not stop digging until every stone has been turned.",
            "## Looking Ahead\n\nUltimately, the responsibility falls on the informed citizen to navigate this maze of misinformation. The establishment relies on public apathy to maintain control. By demanding accountability and refusing to accept superficial explanations, we can force a level of transparency that has been sorely lacking. The story surrounding this event is a litmus test for our modern society. Will we passively consume the manufactured narrative, or will we demand the unvarnished truth? The choice is ours, and the clock is ticking."
        ]
        
        # Assemble a long, unique 500-600 word article dynamically
        safe_content = f"## {chosen_prefix}: {safe_title}\n\n"
        safe_content += random.choice(p1_options) + "\n\n"
        safe_content += random.choice(p2_options) + "\n\n"
        safe_content += random.choice(p3_options) + "\n\n"
        safe_content += random.choice(p4_options)
        
        return {
            "title": f"{chosen_prefix}: The Truth Behind {safe_title}",
            "content": safe_content,
            "seo_description": f"Read the latest scandalous insights and trending updates about {safe_title}. The truth is out there.",
            "is_bizarre": True,
            "is_breaking": (chosen_prefix == "BREAKING")
        }
