"""
User model for PostgreSQL.
"""
from sqlalchemy import Column, String, Boolean, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .base import BaseModel


class User(BaseModel):
    """User model for OAuth authentication."""

    __tablename__ = "users"

    email = Column(String(255), unique=True, nullable=False)
    oauth_provider = Column(String(50), nullable=False)
    oauth_subject = Column(String(255), nullable=False)
    display_name = Column(String(255))
    is_super_user = Column(Boolean, default=False)
    is_site_owner = Column(Boolean, default=False)

    # Relationships
    organisation_members = relationship(
        "OrganisationMember", back_populates="user", cascade="all, delete-orphan"
    )
    assets = relationship("Asset", back_populates="owner", cascade="all, delete-orphan")
    sensor_labels = relationship(
        "SensorLabel", back_populates="user", cascade="all, delete-orphan"
    )
    sensor_alarms = relationship(
        "SensorAlarm", back_populates="created_by_user", cascade="all, delete-orphan"
    )
    notifications = relationship(
        "Notification", back_populates="user", cascade="all, delete-orphan"
    )
    marketplace_listings = relationship(
        "MarketplaceListing",
        back_populates="listed_by_user",
        cascade="all, delete-orphan",
    )
    marketplace_purchases = relationship(
        "MarketplacePurchase",
        back_populates="buyer_user",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        UniqueConstraint("oauth_provider", "oauth_subject", name="uq_user_oauth"),
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, provider={self.oauth_provider})>"