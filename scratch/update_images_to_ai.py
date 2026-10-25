import sqlite3
import urllib.parse
import re

def generate_image_prompt(title: str, is_bizarre: bool = False) -> str:
    title_lower = title.lower()
    if any(w in title_lower for w in ["world series", "baseball", "mlb", "brewers", "rays"]):
        prompt = "cinematic baseball stadium night game dramatic lighting crowd cheering"
    elif any(w in title_lower for w in ["election", "voting", "ballot", "midterm", "senate"]):
        prompt = "american flag patriotic voting booth ballot box dramatic studio lighting"
    elif any(w in title_lower for w in ["football", "nfl", "college football", "sec", "big ten"]):
        prompt = "american football stadium aerial view night game dramatic floodlights"
    elif any(w in title_lower for w in ["hurricane", "storm", "tornado", "nor'easter", "wildfire", "fire"]):
        prompt = "dramatic storm clouds dark sky lightning bolt cinematic weather photography"
    elif any(w in title_lower for w in ["ai", "artificial intelligence", "nuclear", "reactor", "tech", "data center"]):
        prompt = "futuristic server room glowing blue neon light technology cinematic"
    elif any(w in title_lower for w in ["trump", "biden", "president", "white house", "sanctions", "russia"]):
        prompt = "washington dc capitol building dramatic sunset golden hour american flag"
    elif any(w in title_lower for w in ["stock", "economy", "bitcoin", "market", "wall street"]):
        prompt = "stock market trading floor dramatic financial graphs golden light"
    elif any(w in title_lower for w in ["halloween", "horror", "scary", "terrifier", "smile", "clown", "box office"]):
        prompt = "dark gothic halloween night jack o lanterns eerie orange fog cinematic"
    elif any(w in title_lower for w in ["daylight saving", "clock", "time", "sunshine"]):
        prompt = "vintage analog clock golden hour warm sunlight morning fog cinematic"
    elif any(w in title_lower for w in ["immigration", "visa", "green card", "silicon valley", "microsoft"]):
        prompt = "technology office workspace modern city skyline dramatic light rays"
    elif any(w in title_lower for w in ["celebrity", "hollywood", "gossip", "scandal"]):
        prompt = "hollywood walk of fame night neon lights glamour cinematic dramatic"
    elif is_bizarre:
        prompt = "surreal bizarre dark dramatic cinematic photography mysterious shadows"
    else:
        prompt = "dramatic american newspaper journalism editorial bold cinematic photography"
    
    prompt += ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
    return prompt

def build_ai_image_url(title: str, slug: str, is_bizarre: bool = False) -> str:
    prompt = generate_image_prompt(title, is_bizarre)
    encoded = urllib.parse.quote(prompt)
    seed = abs(hash(slug)) % 999999
    return f"https://image.pollinations.ai/prompt/{encoded}?width=800&height=500&seed={seed}&nologo=true"

conn = sqlite3.connect("news.db")
cursor = conn.cursor()

cursor.execute("SELECT id, title, slug, is_bizarre FROM news_articles")
articles = cursor.fetchall()

print(f"Updating {len(articles)} articles with AI-generated image URLs...")
for art_id, title, slug, is_bizarre in articles:
    image_url = build_ai_image_url(title, slug, bool(is_bizarre))
    cursor.execute("UPDATE news_articles SET image_url = ? WHERE id = ?", (image_url, art_id))
    print(f"  [{art_id}] {title[:50]}...")

conn.commit()
conn.close()
print("Done! All articles now use AI-generated Pollinations.ai images.")
