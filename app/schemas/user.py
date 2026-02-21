"""
User schemas for authentication and management.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, validator
from app.models.user import UserRole


class UserBase(BaseModel):
    """Base user schema."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    role: UserRole = UserRole.USER


class UserCreate(UserBase):
    """Schema for user creation."""
    password: str = Field(..., min_length=8)

    @validator("password")
    def password_strength(cls, v):
        """Validate password strength."""
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        return v


class UserUpdate(BaseModel):
    """Schema for user updates."""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None
    organisation_id: Optional[int] = None


class UserInDB(UserBase):
    """User schema as stored in database."""
    id: int
    is_active: bool
    organisation_id: Optional[int]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserResponse(UserInDB):
    """User schema for API responses."""
    pass


class UserLogin(BaseModel):
    """Schema for user login."""
    username: str
    password: str