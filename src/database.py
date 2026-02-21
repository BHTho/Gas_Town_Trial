import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", "sqlite:///./test.db"
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB setup
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
mongo_client = MongoClient(MONGODB_URL)
mongo_db = mongo_client.get_database(os.getenv("MONGODB_DB", "app"))

def get_db():
    """Dependency for SQLAlchemy session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()