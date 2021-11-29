"""add content column to posts table

Revision ID: ff4d46e6bb57
Revises: 99c514322743
Create Date: 2021-11-24 21:32:16.276981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff4d46e6bb57'
down_revision = '99c514322743'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
