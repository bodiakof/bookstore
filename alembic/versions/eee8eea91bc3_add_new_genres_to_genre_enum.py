"""Add new genres to Genre enum

Revision ID: eee8eea91bc3
Revises: 4c56ac6ade89
Create Date: 2025-08-15 09:43:05.108243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eee8eea91bc3'
down_revision: Union[str, Sequence[str], None] = '4c56ac6ade89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add new genres to genre_enum
    op.execute("ALTER TYPE genre_enum ADD VALUE 'MYTHOLOGY'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'MAGICAL_REALISM'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'HORROR'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'DYSTOPIAN'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'CLASSIC'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'THRILLER'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'MYSTERY'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'EPIC_POETRY'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'MEMOIR'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'SELF_HELP'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'PSYCHOLOGY'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'PHILOSOPHY'")
    op.execute("ALTER TYPE genre_enum ADD VALUE 'SCIENCE'")

def downgrade() -> None:
    """Downgrade schema."""
    pass
