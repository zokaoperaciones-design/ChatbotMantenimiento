"""enable_extensions

Revision ID: 0001_enable_extensions
Revises:
Create Date: 2026-05-20 14:30:00.000000

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "0001_enable_extensions"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # pgcrypto: necesario para gen_random_uuid()
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
    # vector: ya viene activado por el script de init, pero hacemos idempotente
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")


def downgrade() -> None:
    # No eliminamos extensiones en downgrade: podrían ser usadas por otros schemas
    pass
