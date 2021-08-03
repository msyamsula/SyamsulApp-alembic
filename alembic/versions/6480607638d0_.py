"""

Revision ID: 6480607638d0
Revises: 8a4b1a5ca3ea
Create Date: 2021-07-23 14:42:08.976725+07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6480607638d0'
down_revision = '8a4b1a5ca3ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('private_message', sa.Column('is_read', sa.BOOLEAN(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('private_message', 'is_read')
    # ### end Alembic commands ###
