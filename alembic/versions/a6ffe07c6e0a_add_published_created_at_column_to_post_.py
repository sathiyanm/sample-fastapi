"""add published, created_at column to post table

Revision ID: a6ffe07c6e0a
Revises: 6bf91ac81183
Create Date: 2024-02-12 18:08:08.854864

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6ffe07c6e0a'
down_revision: Union[str, None] = '6bf91ac81183'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published',  sa.Boolean(), nullable=False, server_default='True'),)
    op.add_column('posts', sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
