# News App API

A RESTful API for a news application built with Python and FastAPI.

## Technologies

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- python-dotenv
- psycopg2

## Features

- REST API built with FastAPI.
- News article management.
- Categories and authors.
- Article statistics (likes and comments).
- Database operations using SQLAlchemy ORM.
- Database migrations with Alembic.
- Data validation using Pydantic.
- Interactive API documentation.

## Project Structure

```text
News_app/
├── app/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── database_models.py
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Nihad-Alek/News_app.git
```

2. Navigate to the project directory:

```bash
cd News_app
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

For macOS/Linux:

```bash
source venv/bin/activate
```

For Windows:

```bash
venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory and add your database connection:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/news_db
```

Replace the values with your PostgreSQL credentials.

## Run the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

## API Documentation

FastAPI provides interactive API documentation:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Goal

This project was developed to gain practical experience in backend development, REST API design, relational databases, and modern Python backend technologies.

## Author

Nihad Alekberov

GitHub: [https://github.com/Nihad-Alek](https://github.com/Nihad-Alek)