from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./news.db"
    GEMINI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    AUTOMATION_API_KEY: Optional[str] = "kronik-admin-123"
    # Gemini free tier = 20 requests/day. One article every 75 min spreads them across the day (~19/day).
    # After enabling billing, set ARTICLE_INTERVAL_MINUTES=5 and ARTICLES_PER_RUN=2 in Render.
    ARTICLE_INTERVAL_MINUTES: int = 75
    ARTICLES_PER_RUN: int = 1

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
