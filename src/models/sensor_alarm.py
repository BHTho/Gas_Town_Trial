"""
SensorAlarm model for PostgreSQL.
"""
import enum
from sqlalchemy import Column, String, ForeignKey, Boolean, Float, DateTime, Enum
from sqlalchemy.orm import relationship

from .base import BaseModel


class AlarmCondition(enum.Enum):
    """Condition for alarm triggering."""

    ABOVE = "above"
    BELOW = "below"
    EQUALS = "equals"


class SensorAlarm(BaseModel):
    """Alarm configuration for sensor readings."""

    __tablename__ = "sensor_alarms"

    sensor_id = Column(
        String(36), ForeignKey("sensors.id", ondelete="CASCADE"), nullable=False
    )
    created_by_user_id = Column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String(255), nullable=False)
    condition = Column(Enum(AlarmCondition), nullable=False)
    threshold = Column(Float, nullable=False)
    notify_email = Column(String(255))
    is_active = Column(Boolean, default=True)
    triggered_state = Column(Boolean, default=False)
    last_triggered_at = Column(DateTime)
    last_reset_at = Column(DateTime)

    # Relationships
    sensor = relationship("Sensor", back_populates="alarms")
    created_by_user = relationship("User", back_populates="sensor_alarms")
    notifications = relationship("Notification", back_populates="alarm", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<SensorAlarm(id={self.id}, name={self.name}, sensor={self.sensor_id})>"