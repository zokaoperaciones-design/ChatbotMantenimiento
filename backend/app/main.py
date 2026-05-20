"""
Chatbot Mantenimiento Industrial — Backend FastAPI
Punto de entrada de la aplicación.
"""

from datetime import datetime, timezone

from fastapi import APIRouter, FastAPI

app = FastAPI(
    title="Chatbot Mantenimiento Industrial — API",
    description="API del sistema RAG de mantenimiento industrial.",
    version="0.1.0",
)

# Router principal con prefijo /api/v1 — endpoints reales se añaden en hitos siguientes
api_v1 = APIRouter(prefix="/api/v1")
app.include_router(api_v1)


@app.get("/health", tags=["system"])
def health() -> dict:
    """Health check del backend. No comprueba dependencias externas todavía."""
    return {
        "status": "ok",
        "service": "backend",
        "version": app.version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
