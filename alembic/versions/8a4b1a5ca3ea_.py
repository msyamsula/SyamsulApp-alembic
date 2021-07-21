"""

Revision ID: 8a4b1a5ca3ea
Revises: 02f76f246b97
Create Date: 2021-07-21 18:25:00.423184+07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a4b1a5ca3ea'
down_revision = '02f76f246b97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('status', sa.String(length=30), server_default='Offline', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'status')
    # ### end Alembic commands ###