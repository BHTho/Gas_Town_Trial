"""
Organisation model for PostgreSQL.
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Organisation(BaseModel):
    """Organisation model for multi-tenancy."""

    __tablename__ = "organisations"

    name = Column(String(255), nullable=False)
    billing_customer_id = Column(String(255))
    subscription_tier = Column(String(50), default="free")

    # Relationships
    members = relationship(
        "OrganisationMember", back_populates="organisation", cascade="all, delete-orphan"
    )
    assets = relationship(
        "Asset", back_populates="organisation", cascade="all, delete-orphan"
    )
    marketplace_listings = relationship(
        "MarketplaceListing",
        back_populates="organisation",
        cascade="all, delete-orphan",
    )
    marketplace_purchases = relationship(
        "MarketplacePurchase",
        back_populates="buyer_organisation",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Organisation(id={self.id}, name={self.name})>"