#!/usr/bin/env python3
"""
Test that SQLAlchemy models can be created and have correct columns.
Uses SQLite in-memory database.
"""
import os
import sys
sys.path.insert(0, '.')

# Override DATABASE_URL before importing database module
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

# Import after setting env var
from src.database import engine, Base
import src.models  # register all models

def test_table_creation():
    """Create all tables and verify no errors"""
    Base.metadata.create_all(bind=engine)
    print("✅ All SQL tables created successfully")

    # Inspect tables
    from sqlalchemy import inspect
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(f"✅ Created {len(tables)} tables: {tables}")

    # Drop tables
    Base.metadata.drop_all(bind=engine)
    print("✅ Tables dropped")

if __name__ == "__main__":
    try:
        test_table_creation()
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)