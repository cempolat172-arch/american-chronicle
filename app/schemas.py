from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ArticleBase(BaseModel):
    title: str
    slug: str
    content: str
    original_url: str
    seo_description: Optional[str] = None
    is_bizarre: Optional[bool] = False
    is_breaking: Optional[bool] = False
    published_at: Optional[datetime] = None

class ArticleCreate(ArticleBase):
    pass

class ArticleResponse(ArticleBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
