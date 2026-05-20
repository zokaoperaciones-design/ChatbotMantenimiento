FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# Dependencias del sistema mínimas
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Instalar dependencias Python primero (mejor cache de capas)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar código (en desarrollo se sobrescribe con bind mount)
COPY . .

EXPOSE 8000

# Hot-reload activado para desarrollo
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
