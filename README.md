# Chatbot Mantenimiento Industrial

Plataforma de IA conversacional especializada en mantenimiento de maquinaria industrial. Sistema RAG con citación exacta de fuentes sobre documentación técnica (manuales, planos, protocolos, históricos de averías).

**Estado:** 🚧 En desarrollo — Hito 1 (cimientos técnicos)

## Stack

- **Backend:** Python 3.11+, FastAPI, SQLAlchemy, Alembic
- **Base de datos:** PostgreSQL 16 + pgvector
- **LLM:** OpenAI GPT-4o-mini (vía API)
- **Frontend:** Next.js 14+ con React 18 y TypeScript *(pendiente)*
- **Orquestación ingesta:** n8n *(pendiente)*
- **Despliegue:** Docker Compose

## Documentación del proyecto

El diseño completo está en el documento `plan_implementacion_chatbot_industrial.md` (no versionado en este repositorio).

## Cómo arrancar (desarrollo)

> Esta sección se completará al cierre del Hito 1.

```bash
# Pendiente
docker compose -f docker-compose.dev.yml up
```

## Hitos

- [ ] **Hito 1** — Cimientos técnicos
- [ ] Hito 2 — Auth y CRUD básico
- [ ] Hito 3 — Ingesta documental
- [ ] Hito 4 — Motor RAG
- [ ] Hito 5 — Chat frontend completo
- [ ] Hito 6 — Endurecimiento y producción

## Licencia

Propietario. Todos los derechos reservados.
