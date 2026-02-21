"""
Dependencies for FastAPI routes.
"""
from app.database import get_db
from .auth import (
    get_current_user,
    get_current_active_user,
    require_role,
    require_admin,
    require_user,
    require_viewer,
)

__all__ = [
    "get_db",
    "get_current_user",
    "get_current_active_user",
    "require_role",
    "require_admin",
    "require_user",
    "require_viewer",
]