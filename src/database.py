import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# SQLAlchemy setup - default to PostgreSQL
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/iot_assets"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Import Base from models (circular import avoided)
from src.models.base import Base

# MongoDB setup
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
mongo_client = MongoClient(MONGODB_URL)
mongo_db = mongo_client.get_database(os.getenv("MONGODB_DB", "iot_assets"))

def get_db():
    """Dependency for SQLAlchemy session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()