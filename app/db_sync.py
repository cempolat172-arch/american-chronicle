"""
Copies articles from the bundled SQLite file (news.db in the repo) into the live database
(Supabase Postgres) on startup. Only articles whose slug is not in the live database yet are added,
so articles written by the automation are never touched or lost.

Workflow stays the same as before: add articles to news.db, push to GitHub, Render redeploys,
new articles appear on the site.
"""
import logging
import os
import sqlite3
from datetime import datetime, timezone

from sqlalchemy import text

from app.database import engine, IS_SQLITE

logger = logging.getLogger(__name__)

SQLITE_PATH = os.path.join(os.getcwd(), "news.db")
COLUMNS = ["title", "slug", "content", "original_url", "seo_description", "keywords", "is_bizarre",
           "is_breaking", "published_at", "created_at", "reaction_shock", "reaction_fire",
           "reaction_clown", "image_url"]


def _to_datetime(value):
    if value is None or isinstance(value, datetime):
        return value
    try:
        dt = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def sync_bundled_articles():
    if IS_SQLITE:
        return  # live DB *is* the bundled file
    if not os.path.exists(SQLITE_PATH):
        logger.info("db_sync: no bundled news.db found, skipping.")
        return

    src = sqlite3.connect(SQLITE_PATH)
    src.row_factory = sqlite3.Row
    src_cols = {r[1] for r in src.execute("PRAGMA table_info(news_articles)")}
    cols = [c for c in COLUMNS if c in src_cols]
    rows = src.execute(f"SELECT {', '.join(cols)} FROM news_articles ORDER BY id").fetchall()
    src.close()

    with engine.begin() as conn:
        existing_slugs = {r[0] for r in conn.execute(text("SELECT slug FROM news_articles"))}
        existing_urls = {r[0] for r in conn.execute(text("SELECT original_url FROM news_articles"))}
        added = updated = 0
        editable = [c for c in ("title", "content", "seo_description", "keywords", "image_url", "published_at")
                    if c in cols]
        for row in rows:
            data = dict(row)
            if data["slug"] in existing_slugs:
                # Hand-written (bundled) article already live: push corrections made in news.db
                values = {c: (_to_datetime(data[c]) if c == "published_at" else data[c]) for c in editable}
                live = conn.execute(text(f"SELECT {', '.join(editable)} FROM news_articles WHERE slug = :slug"),
                                    {"slug": data["slug"]}).mappings().first()
                if live and any(live[c] != values[c] for c in editable):
                    conn.execute(text(f"UPDATE news_articles SET {', '.join(f'{c} = :{c}' for c in editable)} "
                                      f"WHERE slug = :slug"), {**values, "slug": data["slug"]})
                    updated += 1
                continue
            if data["original_url"] in existing_urls:
                continue
            for key in ("published_at", "created_at"):
                if key in data:
                    data[key] = _to_datetime(data[key])
            for key in ("is_bizarre", "is_breaking"):
                if key in data:
                    data[key] = bool(data[key])
            for key in ("reaction_shock", "reaction_fire", "reaction_clown"):
                if key in data and data[key] is None:
                    data[key] = 0
            if not data.get("created_at"):
                data["created_at"] = data.get("published_at") or datetime.now(timezone.utc)
            conn.execute(
                text(f"INSERT INTO news_articles ({', '.join(cols)}) VALUES ({', '.join(':' + c for c in cols)})"),
                data,
            )
            existing_slugs.add(data["slug"])
            existing_urls.add(data["original_url"])
            added += 1
    logger.info(f"db_sync: {added} bundled article(s) added, {updated} updated ({len(rows)} in news.db).")
