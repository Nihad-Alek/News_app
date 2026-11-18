from fastapi import APIRouter , Depends , HTTPException , Query
from sqlalchemy import select
from sqlalchemy.orm import Session , joinedload
from app.database_models import get_db , Article
import re

router = APIRouter(prefix='/api/news' , tags=['news'])

def parse_id(raw_id: str):
    if not re.fullmatch(r'\d+' , raw_id , flags=re.ASCII):
        raise HTTPException(status_code=400 , detail='Id written wrong')
    return int(raw_id)

@router.get('/{id}')
def get_news(id: str , db: Session = Depends(get_db)):
    news_id = parse_id(id)

    stmt = (
    select(Article)
    .options(
        joinedload(Article.category),
        joinedload(Article.author),
        joinedload(Article.stats),
        )
        .where(Article.id == news_id)
        )
    
    article = db.execute(stmt).unique().scalar_one_or_none()

    if article is None:
        raise HTTPException(status_code=404 , detail='Information not found')
    
    s = article.stats
    return {
        "id": article.id,
        "title": article.title,
        "short_description": article.short_description,
        "content": article.content,
        "image_url": article.image_url,
        "created_at": article.created_at,
        "read_time_minutes": article.read_time_minutes,
        "is_trending": article.is_trending,
        "is_breaking": article.is_breaking,
        "is_live": article.is_live,
        "category": article.category,
        "author": article.author,
        "stats": {
            "likes_count": s.likes_count if s else 0,
            "shares_count": s.shares_count if s else 0,
            "bookmarks_count": s.bookmarks_count if s else 0,
            "comments_count": s.comments_count if s else 0,
        }
    }

@router.get('/{id}/related')
def get_news_related(id: str , limit: int = Query(5 , ge=1 , le=20) , db = Session(get_db)):
    news_id = parse_id(id)

    category_id = db.scalar(
        select(Article.category_id).where(Article.id == news_id)
    )
    if category_id is None:
        raise HTTPException(status_code=404 , detail='Infromation not found')

    stmt = (
        select(Article)
        .options(joinedload(Article.category) , joinedload(Article.stats))
        .where(Article.category_id == category_id , Article.id != news_id)
        .order_by(Article.created_at.desc())
        .limit(limit)
    )
    articles = db.execute(stmt).unique().all()
    return [
    {
        "id": a.id,
        "title": a.title,
        "short_description": a.short_description,
        "image_url": a.image_url,
        "category": a.category,
        "stats": {
            "likes_count": a.stats.likes_count if a.stats else 0,
            "shares_count": a.stats.shares_count if a.stats else 0,
            "bookmarks_count": a.stats.bookmarks_count if a.stats else 0,
        }
    }
    for a in articles
    ]