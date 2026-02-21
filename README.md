# Backend API

FastAPI backend project.

## Setup

1. Install dependencies:

```bash
pip install -e .
```

2. Run the development server:

```bash
uvicorn app.main:app --reload
```

## Project Structure

- `app/` - Main application package
  - `main.py` - FastAPI app instance
  - `routers/` - API route modules
  - `models/` - SQLAlchemy models
  - `schemas/` - Pydantic schemas
  - `dependencies/` - Dependency injection
  - `services/` - Business logic
  - `utils/` - Utilities
- `alembic/` - Database migrations
- `tests/` - Test suite

## Development

See `pyproject.toml` for optional development dependencies.

Run tests:

```bash
pytest
```