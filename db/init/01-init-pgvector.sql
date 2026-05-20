-- ============================================
-- Inicialización pgvector
-- ============================================
-- Este script se ejecuta UNA SOLA VEZ cuando el contenedor de Postgres
-- se arranca contra un directorio de datos vacío.
-- Se ejecuta como superusuario sobre la base de datos POSTGRES_DB.
-- ============================================

CREATE EXTENSION IF NOT EXISTS vector;

-- Verificación: log en stdout del contenedor
DO $$
BEGIN
    RAISE NOTICE 'Extensión pgvector instalada correctamente.';
END
$$;
