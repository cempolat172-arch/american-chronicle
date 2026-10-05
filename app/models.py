from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base

class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, index=True, nullable=False)
    content = Column(Text, nullable=False)
    original_url = Column(String, unique=True, index=True, nullable=False)
    seo_description = Column(String, nullable=True)
    is_bizarre = Column(Boolean, default=False)
    is_breaking = Column(Boolean, default=False)
    published_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    reaction_shock = Column(Integer, default=0)
    reaction_fire = Column(Integer, default=0)
    reaction_clown = Column(Integer, default=0)
    
    image_url = Column(String, nullable=True)
