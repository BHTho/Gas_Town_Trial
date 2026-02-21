"""
SensorLabel model for PostgreSQL.
"""
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import BaseModel


class SensorLabel(BaseModel):
    """Label assigned by users to sensors."""

    __tablename__ = "sensor_labels"

    sensor_id = Column(
        String(36), ForeignKey("sensors.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    label = Column(String(100), nullable=False)
    colour = Column(String(7))  # hex color code

    # Relationships
    sensor = relationship("Sensor", back_populates="labels")
    user = relationship("User", back_populates="sensor_labels")

    # Unique constraint (sensor_id, label)
    __table_args__ = (
        UniqueConstraint('sensor_id', 'label', name='uq_sensor_label'),
    )

    def __repr__(self) -> str:
        return f"<SensorLabel(sensor={self.sensor_id}, label={self.label})>"