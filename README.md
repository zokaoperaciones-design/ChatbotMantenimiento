# Chatbot Mantenimiento Industrial

Plataforma de IA conversacional especializada en mantenimiento de maquinaria industrial. Sistema RAG con citación exacta de fuentes sobre documentación técnica (manuales, planos, protocolos, históricos de averías).

**Estado:** 🚧 En desarrollo — Hito 1 completado ✅

## Stack

- **Backend:** Python 3.11, FastAPI, SQLAlchemy 2.0, Alembic
- **Base de datos:** PostgreSQL 16 + pgvector
- **LLM:** OpenAI GPT-4o-mini *(pendiente Hito 4)*
- **Frontend:** Next.js 14+ con React 18 *(pendiente Hito 5)*
- **Orquestación ingesta:** n8n *(pendiente Hito 3)*
- **Despliegue:** Docker Compose

## Documentación del proyecto

El diseño completo está en el documento `plan_implementacion_chatbot_industrial.md` (no versionado en este repositorio).

## Arranque rápido (desarrollo)

### Requisitos previos
- Docker Desktop con WSL2 (Windows) o Docker Engine (Linux).
- Git.

### Primer arranque

```powershell
# 1. Clonar el repositorio
git clone https://github.com/zokaoperaciones-design/ChatbotMantenimiento.git
cd ChatbotMantenimiento

# 2. Crear .env a partir del ejemplo
Copy-Item .env.example .env
# (Editar .env si quieres cambiar contraseñas/credenciales)

# 3. Levantar todo
docker compose -f docker-compose.dev.yml up -d --build

# 4. Aplicar migraciones de base de datos
docker compose -f docker-compose.dev.yml exec backend alembic upgrade head
```

### Verificación

```powershell
# Health check del backend
Invoke-WebRequest -Uri "http://localhost:8000/health" -UseBasicParsing | Select-Object -ExpandProperty Content

# Health check de conexión con BD
Invoke-WebRequest -Uri "http://localhost:8000/health/db" -UseBasicParsing | Select-Object -ExpandProperty Content

# Swagger UI
# http://localhost:8000/docs
```

### Comandos útiles

```powershell
# Parar (mantiene datos)
docker compose -f docker-compose.dev.yml stop

# Arrancar de nuevo
docker compose -f docker-compose.dev.yml start

# Ver logs en vivo
docker compose -f docker-compose.dev.yml logs -f backend

# Reset COMPLETO (⚠️ borra datos de BD)
docker compose -f docker-compose.dev.yml down
docker volume rm chatbot_postgres_data
```

### Migraciones

```powershell
# Aplicar migraciones pendientes
docker compose -f docker-compose.dev.yml exec backend alembic upgrade head

# Ver estado actual
docker compose -f docker-compose.dev.yml exec backend alembic current

# Generar nueva migración tras cambios en modelos
docker compose -f docker-compose.dev.yml exec backend alembic revision --autogenerate -m "descripcion_del_cambio"
```

## Estructura del repositorio

```
.
├── backend/                    # API FastAPI
│   ├── alembic/                # Migraciones de base de datos
│   ├── app/
│   │   ├── api/                # Endpoints HTTP (pendientes)
│   │   ├── core/               # config, database
│   │   ├── models/             # Modelos SQLAlchemy
│   │   ├── schemas/            # Pydantic (pendientes)
│   │   ├── services/           # Lógica de negocio (pendientes)
│   │   └── main.py
│   ├── tests/                  # Tests (pendientes)
│   ├── Dockerfile
│   └── requirements.txt
├── db/init/                    # Scripts SQL de inicialización
├── frontend/                   # Next.js (pendiente)
├── n8n/                        # Workflows n8n (pendiente)
├── docker-compose.dev.yml
├── .env.example
└── README.md
```

## Hitos

- [x] **Hito 1** — Cimientos técnicos
- [ ] Hito 2 — Auth y CRUD básico
- [ ] Hito 3 — Ingesta documental
- [ ] Hito 4 — Motor RAG
- [ ] Hito 5 — Chat frontend completo
- [ ] Hito 6 — Endurecimiento y producción

## Licencia

Propietario. Todos los derechos reservados.
