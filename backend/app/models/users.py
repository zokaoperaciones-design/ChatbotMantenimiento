"""Modelo de usuarios del sistema."""

from __future__ import annotations

import enum
import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Enum as PgEnum
from sqlalchemy import String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.conversations import Conversation


class UserRole(str, enum.Enum):
    admin = "admin"
    supervisor = "supervisor"
    tecnico = "tecnico"


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    rol: Mapped[UserRole] = mapped_column(
        PgEnum(UserRole, name="user_role", create_type=True),
        nullable=False,
    )

    conversations: Mapped[list[Conversation]] = relationship(
        back_populates="user",
        passive_deletes=True,
    )
