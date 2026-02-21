"""
Notification model for PostgreSQL.
"""
import enum
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, Boolean, Float, Text, DateTime, Enum
from sqlalchemy.orm import relationship

from .base import BaseModel


class NotificationCondition(enum.Enum):
    """Condition that triggered notification."""

    ABOVE = "above"
    BELOW = "below"
    EQUALS = "equals"


class Notification(BaseModel):
    """Notification sent to users about alarm triggers."""

    __tablename__ = "notifications"

    alarm_id = Column(
        String(36), ForeignKey("sensor_alarms.id", ondelete="SET NULL")
    )
    sensor_id = Column(
        String(36), ForeignKey("sensors.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    reading_value = Column(Float, nullable=False)
    threshold = Column(Float, nullable=False)
    condition = Column(Enum(NotificationCondition), nullable=False)
    message = Column(Text, nullable=False)
    is_read = Column(Boolean, default=False)
    email_sent = Column(Boolean, default=False)
    triggered_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    alarm = relationship("SensorAlarm", back_populates="notifications")
    sensor = relationship("Sensor", back_populates="notifications")
    user = relationship("User", back_populates="notifications")

    def __repr__(self) -> str:
        return f"<Notification(id={self.id}, user={self.user_id}, is_read={self.is_read})>"