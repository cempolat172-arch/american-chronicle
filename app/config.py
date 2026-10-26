from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./news.db"
    GEMINI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    AUTOMATION_API_KEY: Optional[str] = "kronik-admin-123"
    # Free tier: Flash ~20/day, then Flash-Lite (~500/day each) and Gemma take over automatically.
    # One article every 30 min = ~48 articles/day. Change in Render (Environment) without code changes.
    ARTICLE_INTERVAL_MINUTES: int = 30
    ARTICLES_PER_RUN: int = 1

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
