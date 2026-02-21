#!/usr/bin/env python3
"""
Initialize database - create SQL tables and MongoDB indexes.
"""
import sys
sys.path.insert(0, '.')

from src.database import engine, Base
from src.models.sql import User, Post
from src.mongodb.indexes import create_indexes

def init_sql():
    """Create SQL tables"""
    Base.metadata.create_all(bind=engine)
    print("SQL tables created successfully")

if __name__ == "__main__":
    print("Initializing database...")
    init_sql()
    create_indexes()
    print("Database initialization complete")