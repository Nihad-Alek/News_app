import os
from dotenv import load_dotenv
from sqlalchemy import create_engine , ForeignKey , String , Boolean , Text , DateTime
from sqlalchemy.orm import sessionmaker , DeclarativeBase , Mapped , mapped_column , relationship
from datetime import datetime , timezone


load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL , connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine , autoflush=False , autocommit=False)

def get_db():
    db = SessionLocal()
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
    slug: Mapped[str] = mapped_column(String(50) , unique=True , nullable=False)
    badge_color: Mapped[str | None] = mapped_column(String(20))

class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150) , nullable=False)
    avatar_url: Mapped[str | None] = mapped_column(String(500))
    bio: Mapped[str | None] = mapped_column(Text)
    twitter_handle: Mapped[str | None] = mapped_column(String(100))

class Article(Base):
    __tablename__ = 'Articles'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(300) , nullable=False)
    short_description: Mapped[str] = mapped_column(Text , nullable=False)
    content: Mapped[str] = mapped_column(Text , nullable=False)
    image_url: Mapped[str] = mapped_column(String(500) , nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    read_time_minutes: Mapped[int] = mapped_column(nullable=False)
    is_trending: Mapped[bool] = mapped_column(Boolean , default=False)
    is_breaking: Mapped[bool] = mapped_column(Boolean , default=False)
    is_live: Mapped[bool] = mapped_column(Boolean , default=False)
    is_editors_pick: Mapped[bool] = mapped_column(Boolean, default=False)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False)
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'))
    created_at: Mapped[datetime] =  mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc),
    nullable=False)
    category: Mapped['Category'] = relationship()
    author: Mapped['Author'] = relationship()
    stats: Mapped['ArticleStats | None'] = relationship(back_populates='article' , uselist=False)

class ArticleStats(Base):
    __tablename__ = 'Article_stats'

    id: Mapped[int] = mapped_column(primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey('Articles.id'))
    likes_count: Mapped[int] = mapped_column(default=0 , nullable=False)
    shares_count: Mapped[int] = mapped_column(default=0 , nullable=False)
    bookmarks_count: Mapped[int] = mapped_column(default=0 , nullable=False)
    comments_count: Mapped[int] = mapped_column(default=0 , nullable=False)
    article: Mapped['Article'] = relationship(back_populates='stats')