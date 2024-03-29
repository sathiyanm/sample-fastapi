"""add foreign-key to post table

Revision ID: 6bf91ac81183
Revises: c48fc1f985e7
Create Date: 2024-02-12 17:47:33.037742

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bf91ac81183'
down_revision: Union[str, None] = 'c48fc1f985e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key("fk_post_users", source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('fk_post_users', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
