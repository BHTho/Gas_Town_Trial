# Database Schemas

This project defines database structures using SQLAlchemy (relational) and MongoDB (document) with appropriate indexes.

## Assumptions

Given the lack of specific domain requirements, the following assumptions were made:

1. **SQLAlchemy models** represent a typical blog-like application with Users and Posts
2. **MongoDB indexes** support logging and event tracking systems
3. **Database choice**: SQLite for simplicity, MongoDB local for document storage
4. **Environment configuration** via `.env` file

These schemas can be easily extended or modified when actual domain requirements are provided.

## Models

### SQLAlchemy Models (in `src/models/sql.py`)

- **User**: `users` table with authentication fields and relationship to posts
- **Post**: `posts` table with content and foreign key to author

### MongoDB Indexes (in `src/mongodb/indexes.py`)

- **logs collection**: Indexes on timestamp, level+timestamp, service+timestamp
- **events collection**: Indexes on event_type+created_at, user_id+created_at, session_id
- **users collection**: Unique indexes on email and username (if MongoDB used for user profiles)

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy environment file:
   ```bash
   cp .env.example .env
   ```

3. Initialize databases:
   ```bash
   python scripts/init_db.py
   ```

This will create SQL tables and MongoDB indexes.

## Configuration

- `DATABASE_URL`: SQLAlchemy database URL (default: SQLite `./app.db`)
- `MONGODB_URL`: MongoDB connection string (default: `mongodb://localhost:27017`)
- `MONGODB_DB`: MongoDB database name (default: `app`)

## Usage

Import models from `src.models.sql` and use `SessionLocal` from `src.database` for SQL operations.

Use `mongo_db` from `src.database` for MongoDB operations.

## Extending

Add new SQLAlchemy models in `src/models/` and import them in `scripts/init_db.py` to ensure table creation.

Add new MongoDB indexes in `src/mongodb/indexes.py`.