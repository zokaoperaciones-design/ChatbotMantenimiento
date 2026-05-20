"""
Chatbot Mantenimiento Industrial — Backend FastAPI
Punto de entrada de la aplicación.
"""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db

app = FastAPI(
    title="Chatbot Mantenimiento Industrial — API",
    description="API del sistema RAG de mantenimiento industrial.",
    version="0.1.0",
)

# Router principal — endpoints reales se añaden en hitos siguientes
api_v1 = APIRouter(prefix="/api/v1")
app.include_router(api_v1)


@app.get("/health", tags=["system"])
def health() -> dict:
    """Health check del backend. No comprueba dependencias externas."""
    return {
        "status": "ok",
        "service": "backend",
        "version": app.version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/health/db", tags=["system"])
def health_db(db: Session = Depends(get_db)) -> dict:
    """Verifica conectividad con PostgreSQL y disponibilidad de pgvector."""
    try:
        db.execute(text("SELECT 1"))
        vector_row = db.execute(
            text("SELECT extversion FROM pg_extension WHERE extname = 'vector'")
        ).first()
        pgvector_version = vector_row[0] if vector_row else None
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Database not reachable: {exc}",
        ) from exc

    return {
        "status": "ok",
        "database": "connected",
        "pgvector_version": pgvector_version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
