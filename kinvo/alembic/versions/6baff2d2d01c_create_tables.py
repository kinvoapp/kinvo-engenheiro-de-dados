"""Create tables

Revision ID: 6baff2d2d01c
Revises: 
Create Date: 2021-09-06 15:28:24.003348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6baff2d2d01c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    inspector = sa.engine.reflection.Inspector.from_engine(conn)
    tables = inspector.get_table_names()

    if 'breeds' not in tables:

        op.create_table(
            'news',
            sa.Column('id', sa.Integer, primary_key=True, index=True),
            sa.Column('title', sa.Text, nullable=False),
            sa.Column('link', sa.Text, unique=True, nullable=False),
            sa.Column('content', sa.Text, nullable=False),
            sa.Column('pub_date', sa.DateTime, nullable=False),
        )

    if 'features' not in tables:
        op.create_table(
            'entities',
            sa.Column('id', sa.Integer, primary_key=True, index=True),
            sa.Column('text', sa.String(50), nullable=False),
            sa.Column('entity', sa.String(10), nullable=False),

            sa.Column('news_id', sa.Integer, sa.ForeignKey("news.id")),
        )


def downgrade():
    pass
