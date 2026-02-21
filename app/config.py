import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    api_title: str = "Backend API"
    api_version: str = "0.1.0"
    api_description: str = "FastAPI backend"

    # Database
    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/dbname")
    database_echo: bool = os.getenv("DATABASE_ECHO", "false").lower() == "true"

    # Security
    secret_key: str = os.getenv("SECRET_KEY", "change_this_in_production")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # CORS
    cors_origins: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()