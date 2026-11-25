from app.database_models import Base , engine

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")