"""
Configuración de SQLAlchemy: engine, sesión y Base declarativa.
"""

from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=False,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


class Base(DeclarativeBase):
    """Clase base de todos los modelos ORM."""


def get_db() -> Generator[Session, None, None]:
    """Dependencia FastAPI para obtener una sesión de BD por request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
