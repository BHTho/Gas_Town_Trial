"""
MarketplaceListing model for PostgreSQL.
"""
from sqlalchemy import Column, String, ForeignKey, Integer, Boolean, Text, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class MarketplaceListing(BaseModel):
    """Listing of asset data in marketplace."""

    __tablename__ = "marketplace_listings"

    asset_id = Column(
        String(36), ForeignKey("assets.id", ondelete="CASCADE"), nullable=False
    )
    organisation_id = Column(
        String(36), ForeignKey("organisations.id", ondelete="CASCADE")
    )
    listed_by_user_id = Column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    price_per_1000_rows = Column(Integer, nullable=False)
    hidden_columns = Column(JSON, default=list)
    is_active = Column(Boolean, default=True)
    description = Column(Text)

    # Relationships
    asset = relationship("Asset", back_populates="marketplace_listings")
    organisation = relationship("Organisation", back_populates="marketplace_listings")
    listed_by_user = relationship("User", back_populates="marketplace_listings")
    purchases = relationship(
        "MarketplacePurchase", back_populates="listing", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<MarketplaceListing(id={self.id}, asset={self.asset_id}, price={self.price_per_1000_rows})>"