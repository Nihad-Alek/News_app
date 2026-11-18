import os
from dotenv import load_dotenv
from sqlalchemy import create_engine , ForeignKey , String , Boolean , Text , DateTime
from sqlalchemy.orm import sessionmaker , DeclarativeBase , Mapped , mapped_column , relationship
from datetime import datetime


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine , autoflush=False)

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    slug: Mapped[str] = mapped_column(String(100))
    bagged_colum: Mapped[str | None] = mapped_column(String(20))

class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))
    avatar_url: Mapped[str | None] = mapped_column(String(500))
    bio: Mapped[str | None] = mapped_column(Text)
    twitter_handle: Mapped[str | None] = mapped_column(String(100))

class Article(Base):
    __tablename__ = 'Articles'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(300))
    short_description: Mapped[str | None] = mapped_column(Text)
    content: Mapped[str] = mapped_column(Text)
    image_url: Mapped[str | None] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime)
    read_time_minutes: Mapped[int | None]
    is_trending: Mapped[bool] = mapped_column(Boolean , default=False)
    is_breaking: Mapped[bool] = mapped_column(Boolean , default=False)
    is_live: Mapped[bool] = mapped_column(Boolean , default=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('author.id'))

    category: Mapped['Category'] = relationship()
    author: Mapped['Author'] = relationship()
    stats: Mapped['ArticleStats | None'] = relationship(back_populates='article' , uselist=False)

class ArticleStats(Base):
    __tablename__ = 'article_stats'

    article_id: Mapped[int] = mapped_column(
        ForeignKey('articles.id' , primary_key=True)
    )
    likes_count: Mapped[int] = mapped_column(default=0)
    shares_count: Mapped[int] = mapped_column(default=0)
    bookmarks_count: Mapped[int] = mapped_column(default=0)
    comments_count: Mapped[int] = mapped_column(default=0)

    article: Mapped['Article'] = relationship(back_populates='stats')