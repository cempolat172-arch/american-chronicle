from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./news.db"
    GEMINI_API_KEY: Optional[str] = None
    ANTHROPIC_API_KEY: Optional[str] = None
    AUTOMATION_API_KEY: Optional[str] = "kronik-admin-123"
    # Automated publishing pace: run every 10 minutes, up to 2 articles per batch
    ARTICLE_INTERVAL_MINUTES: int = 10
    ARTICLES_PER_RUN: int = 2

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
