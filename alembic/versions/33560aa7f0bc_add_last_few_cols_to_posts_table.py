"""add last few cols to posts table

Revision ID: 33560aa7f0bc
Revises: 64e38557f26f
Create Date: 2021-11-24 21:52:07.513889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33560aa7f0bc'
down_revision = '64e38557f26f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
                  sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))

    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))

    pass


def downgrade():
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
    pass
