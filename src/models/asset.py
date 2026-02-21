"""
Asset model for PostgreSQL.
"""
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class Asset(BaseModel):
    """Asset model for IoT devices."""

    __tablename__ = "assets"

    organisation_id = Column(
        String(36), ForeignKey("organisations.id", ondelete="CASCADE")
    )
    owner_user_id = Column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String(255), nullable=False)
    manufacturer = Column(String(255))
    make = Column(String(255))
    model = Column(String(255))
    year = Column(Integer)
    serial_number = Column(String(255))
    asset_model_key = Column(String(500))  # normalized: manufacturer+make+model+year
    data_sharing_enabled = Column(Boolean, default=False)
    asset_metadata = Column('metadata', JSON, default=dict)

    # Relationships
    organisation = relationship("Organisation", back_populates="assets")
    owner = relationship("User", back_populates="assets")
    sensors = relationship("Sensor", back_populates="asset", cascade="all, delete-orphan")
    marketplace_listings = relationship(
        "MarketplaceListing", back_populates="asset", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Asset(id={self.id}, name={self.name}, org={self.organisation_id})>"