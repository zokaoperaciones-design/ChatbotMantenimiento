"""Modelos del dominio industrial: marcas y máquinas."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.models.documents import Document


class Brand(Base):
    __tablename__ = "brands"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    nombre: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    pais: Mapped[str | None] = mapped_column(String(80), nullable=True)

    machines: Mapped[list[Machine]] = relationship(
        back_populates="brand",
        cascade="all, delete-orphan",
    )


class Machine(Base):
    __tablename__ = "machines"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    brand_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("brands.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    modelo: Mapped[str] = mapped_column(String(120), nullable=False)
    numero_serie: Mapped[str | None] = mapped_column(String(120), nullable=True)
    ubicacion: Mapped[str | None] = mapped_column(String(200), nullable=True)

    brand: Mapped[Brand] = relationship(back_populates="machines")
    documents: Mapped[list[Document]] = relationship(
        back_populates="machine",
        cascade="all, delete-orphan",
    )
