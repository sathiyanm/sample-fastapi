"""add content column to posts table

Revision ID: c3c18c703758
Revises: fe1079788a61
Create Date: 2024-02-12 16:20:20.396847

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3c18c703758'
down_revision: Union[str, None] = 'fe1079788a61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content') 
    pass
