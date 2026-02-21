"""
MarketplacePurchase model for PostgreSQL.
"""
import enum
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, Integer, DateTime, Enum
from sqlalchemy.orm import relationship

from .base import BaseModel


class PurchaseStatus(enum.Enum):
    """Status of marketplace purchase."""

    PENDING = "pending"
    COMPLETED = "completed"
    REFUNDED = "refunded"


class MarketplacePurchase(BaseModel):
    """Purchase of marketplace listing data."""

    __tablename__ = "marketplace_purchases"

    listing_id = Column(
        String(36), ForeignKey("marketplace_listings.id", ondelete="CASCADE"), nullable=False
    )
    buyer_user_id = Column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    buyer_organisation_id = Column(
        String(36), ForeignKey("organisations.id", ondelete="SET NULL")
    )
    row_count = Column(Integer, nullable=False)
    gross_amount = Column(Integer, nullable=False)
    seller_fee_amount = Column(Integer, nullable=False)
    buyer_fee_amount = Column(Integer, nullable=False)
    net_seller_amount = Column(Integer, nullable=False)
    polar_payment_id = Column(String(255))
    status = Column(Enum(PurchaseStatus), nullable=False, default=PurchaseStatus.PENDING)
    purchased_at = Column(DateTime, default=datetime.utcnow)
    download_expires_at = Column(DateTime)

    # Relationships
    listing = relationship("MarketplaceListing", back_populates="purchases")
    buyer_user = relationship("User", back_populates="marketplace_purchases")
    buyer_organisation = relationship("Organisation", back_populates="marketplace_purchases")

    def __repr__(self) -> str:
        return f"<MarketplacePurchase(id={self.id}, listing={self.listing_id}, status={self.status})>"