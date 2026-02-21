"""
Sensor model for PostgreSQL.
"""
import enum
from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from .base import BaseModel


class AccuracyClass(enum.Enum):
    """Accuracy classification for sensors."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    INDUSTRIAL = "industrial"


class Sensor(BaseModel):
    """Sensor model attached to assets."""

    __tablename__ = "sensors"

    asset_id = Column(
        String(36), ForeignKey("assets.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String(255), nullable=False)
    sensor_type = Column(String(100), nullable=False)
    sensor_manufacturer = Column(String(255))
    sensor_model = Column(String(255))
    accuracy_class = Column(Enum(AccuracyClass))
    unit = Column(String(50), nullable=False)
    api_key_hash = Column(String(255), nullable=False)  # hashed API key
    ingest_endpoint_slug = Column(String(100), unique=True, nullable=False)

    # Relationships
    asset = relationship("Asset", back_populates="sensors")
    labels = relationship("SensorLabel", back_populates="sensor", cascade="all, delete-orphan")
    alarms = relationship("SensorAlarm", back_populates="sensor", cascade="all, delete-orphan")
    notifications = relationship("Notification", back_populates="sensor", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Sensor(id={self.id}, name={self.name}, asset={self.asset_id})>"