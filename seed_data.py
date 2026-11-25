from app.database_models import SessionLocal, Category , Author , Article , ArticleStats
from sqlalchemy import select

db = SessionLocal()
'''
categories = [
    Category(name="Politics", slug="politics", badge_color="#E74C3C"),
    Category(name="Business", slug="business", badge_color="#3498DB"),
    Category(name="Sports", slug="sports", badge_color="#2A8952"),
    Category(name="World", slug="world", badge_color="#9B59B6"),
    Category(name="Travel", slug="travel", badge_color="#F39C12"),
    Category(name="Health", slug="health", badge_color="#1ABC9C"),
    Category(name="Think", slug="think", badge_color="#34495E"),
]
'''
'''
authors = [
    Author(
        name="Lucy Hiddleston",
        avatar_url="https://example.com/lucy.jpg",
        bio="Journalist covering politics and international affairs.",
        twitter_handle="@lucyhiddleston"
    ),
    Author(
        name="Caroline Casey",
        avatar_url="https://example.com/caroline.jpg",
        bio="Business and technology journalist.",
        twitter_handle="@carolinecasey"
    ),
    Author(
        name="James Wilson",
        avatar_url="https://example.com/james.jpg",
        bio="Sports and world news journalist.",
        twitter_handle="@jameswilson"
    )
]
'''


db = SessionLocal()

try:
    categories = {
        category.slug: category.id
        for category in db.scalars(select(Category)).all()
    }

    authors = {
        author.name: author.id
        for author in db.scalars(select(Author)).all()
    }

    articles_data = [
        {
            "title": "New Economic Policy Announced",
            "short_description": "The government has introduced a new economic strategy.",
            "content": """The government has announced a new economic policy aimed at improving the country's financial stability.

The plan focuses on supporting small businesses and encouraging private investment.

Officials believe that these changes will create new employment opportunities.

Economists have welcomed some parts of the proposal but warned that implementation will be challenging.

The government plans to review the results during the next financial year.""",
            "image_url": "https://example.com/economy.jpg",
            "category_id": categories["business"],
            "author_id": authors["Lucy Hiddleston"],
            "read_time_minutes": 5,
            "is_trending": True,
            "is_featured": True
        },
        {
            "title": "Major Political Changes Expected",
            "short_description": "Several political reforms are expected this year.",
            "content": "Political leaders are discussing a series of important reforms. The proposals could change several government policies.",
            "image_url": "https://example.com/politics.jpg",
            "category_id": categories["politics"],
            "author_id": authors["Lucy Hiddleston"],
            "read_time_minutes": 4,
            "is_breaking": True
        },
        {
            "title": "International Leaders Meet for Summit",
            "short_description": "World leaders have gathered to discuss international cooperation.",
            "content": "Leaders from several countries have arrived for an international summit. The discussions will focus on security, trade and cooperation.",
            "image_url": "https://example.com/summit.jpg",
            "category_id": categories["world"],
            "author_id": authors["Caroline Casey"],
            "read_time_minutes": 6,
            "is_breaking": True
        },
        {
            "title": "Live Updates: Global Climate Conference",
            "short_description": "Follow the latest developments from the climate conference.",
            "content": "The international climate conference is taking place today. Representatives are discussing environmental protection and renewable energy.",
            "image_url": "https://example.com/climate.jpg",
            "category_id": categories["world"],
            "author_id": authors["James Wilson"],
            "read_time_minutes": 3,
            "is_live": True
        },
        {
            "title": "The Future of Artificial Intelligence",
            "short_description": "Artificial intelligence continues to transform modern industries.",
            "content": "Artificial intelligence is becoming an important part of everyday life. Companies are investing heavily in new technologies.",
            "image_url": "https://example.com/ai.jpg",
            "category_id": categories["think"],
            "author_id": authors["Caroline Casey"],
            "read_time_minutes": 7,
            "is_editors_pick": True
        },
        {
            "title": "Championship Final Ends Dramatically",
            "short_description": "A dramatic final has surprised sports fans around the world.",
            "content": "The championship final delivered an exciting match. Both teams demonstrated excellent performance throughout the game.",
            "image_url": "https://example.com/sports.jpg",
            "category_id": categories["sports"],
            "author_id": authors["James Wilson"],
            "read_time_minutes": 4,
            "is_editors_pick": True
        },
        {
            "title": "Top Destinations for Summer Travel",
            "short_description": "Travel experts recommend several destinations for summer holidays.",
            "content": "Summer travel is becoming increasingly popular. Many tourists are choosing destinations with beautiful beaches and cultural attractions.",
            "image_url": "https://example.com/travel.jpg",
            "category_id": categories["travel"],
            "author_id": authors["Lucy Hiddleston"],
            "read_time_minutes": 5,
            "is_editors_pick": True
        },
        {
            "title": "New Research on Healthy Eating",
            "short_description": "Researchers have published new findings about healthy diets.",
            "content": "A new study examines the relationship between nutrition and long-term health. Researchers recommend a balanced diet.",
            "image_url": "https://example.com/health.jpg",
            "category_id": categories["health"],
            "author_id": authors["Caroline Casey"],
            "read_time_minutes": 4
        },
        {
            "title": "Global Markets Show Positive Growth",
            "short_description": "Financial markets have demonstrated positive movement.",
            "content": "Several international markets have reported growth. Investors are watching economic indicators closely.",
            "image_url": "https://example.com/markets.jpg",
            "category_id": categories["business"],
            "author_id": authors["James Wilson"],
            "read_time_minutes": 5
        },
        {
            "title": "New Discoveries in Space Exploration",
            "short_description": "Scientists have shared new findings about distant planets.",
            "content": "Space researchers continue to explore distant planets. New observations could help scientists understand the universe.",
            "image_url": "https://example.com/space.jpg",
            "category_id": categories["think"],
            "author_id": authors["Lucy Hiddleston"],
            "read_time_minutes": 6
        },
        {
            "title": "National Team Prepares for Next Tournament",
            "short_description": "The national team has started preparations for an upcoming tournament.",
            "content": "The national team has begun its training programme. Coaches are evaluating players and preparing new strategies.",
            "image_url": "https://example.com/team.jpg",
            "category_id": categories["sports"],
            "author_id": authors["James Wilson"],
            "read_time_minutes": 3
        },
        {
            "title": "Cities Invest in Green Transportation",
            "short_description": "Several cities are investing in environmentally friendly transport.",
            "content": "Urban authorities are introducing new transportation projects. The goal is to reduce pollution and improve public transport.",
            "image_url": "https://example.com/transport.jpg",
            "category_id": categories["world"],
            "author_id": authors["Caroline Casey"],
            "read_time_minutes": 5
        }
    ]

    added_count = 0

    for data in articles_data:
        existing = db.scalar(
            select(Article).where(Article.title == data["title"])
        )

        if existing:
            continue

        article = Article(**data)
        db.add(article)
        db.flush()

        stats = ArticleStats(
            article_id=article.id,
            likes_count=0,
            shares_count=0,
            bookmarks_count=0,
            comments_count=0
        )

        db.add(stats)
        added_count += 1

    db.commit()
    print(f"{added_count} articles added successfully!")

except Exception as error:
    db.rollback()
    print(error)

finally:
    db.close()

'''
try:
    db.add_all()
    db.commit()
except Exception as error:
    db.rollback()
    print(error)
finally:
    db.close()
'''