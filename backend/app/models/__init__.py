"""
Modelos ORM del sistema.

Este módulo importa todos los modelos para que estén registrados
en Base.metadata y Alembic los detecte al generar migraciones.
"""

from app.models.conversations import Citation, Conversation, Message, MessageRole
from app.models.documents import Chunk, Document, Embedding
from app.models.industrial import Brand, Machine
from app.models.ops import AuditLog, LLMUsage
from app.models.users import User, UserRole

__all__ = [
    "Brand",
    "Machine",
    "Document",
    "Chunk",
    "Embedding",
    "User",
    "UserRole",
    "Conversation",
    "Message",
    "MessageRole",
    "Citation",
    "AuditLog",
    "LLMUsage",
]
