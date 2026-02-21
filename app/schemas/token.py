"""
Token schemas for authentication.
"""
from pydantic import BaseModel
from typing import Optional


class Token(BaseModel):
    """Token response schema."""
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None


class TokenPayload(BaseModel):
    """Payload decoded from JWT token."""
    sub: str  # subject (user identifier)
    exp: int  # expiration timestamp
    role: Optional[str] = None
    org_id: Optional[int] = None


class RefreshTokenRequest(BaseModel):
    """Refresh token request schema."""
    refresh_token: str