"""
OrganisationMember model for PostgreSQL.
"""
import enum
from sqlalchemy import Column, String, ForeignKey, Enum, JSON
from sqlalchemy.orm import relationship

from .base import BaseModel


class OrganisationRole(enum.Enum):
    """Roles within an organisation."""

    OWNER = "owner"
    ADMIN = "admin"
    WORKER = "worker"
    VIEWER = "viewer"


class OrganisationMember(BaseModel):
    """Organisation membership with role and permissions."""

    __tablename__ = "organisation_members"

    organisation_id = Column(
        String(36), ForeignKey("organisations.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    role = Column(Enum(OrganisationRole), nullable=False)
    permissions = Column(JSON, default=dict)

    # Relationships
    organisation = relationship("Organisation", back_populates="members")
    user = relationship("User", back_populates="organisation_members")

    __table_args__ = ()

    def __repr__(self) -> str:
        return f"<OrganisationMember(org={self.organisation_id}, user={self.user_id}, role={self.role})>"