"""
AuditLog model for PostgreSQL.
"""
from sqlalchemy import Column, String, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class AuditLog(BaseModel):
    """Audit log for site admin actions."""

    __tablename__ = "audit_logs"

    action = Column(String(100), nullable=False)
    actor_user_id = Column(
        String(36), ForeignKey("users.id", ondelete="SET NULL")
    )
    target_user_id = Column(
        String(36), ForeignKey("users.id", ondelete="SET NULL")
    )
    target_organisation_id = Column(
        String(36), ForeignKey("organisations.id", ondelete="SET NULL")
    )
    details = Column(JSON, default=dict)
    ip_address = Column(String(39))  # IPv6 max length, compatible with all databases
    user_agent = Column(Text)

    # Relationships
    actor_user = relationship("User", foreign_keys=[actor_user_id])
    target_user = relationship("User", foreign_keys=[target_user_id])
    target_organisation = relationship("Organisation", foreign_keys=[target_organisation_id])

    def __repr__(self) -> str:
        return f"<AuditLog(id={self.id}, action={self.action})>"