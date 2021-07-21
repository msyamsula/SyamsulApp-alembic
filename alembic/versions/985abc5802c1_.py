"""

Revision ID: 985abc5802c1
Revises: 25a53e679336
Create Date: 2021-07-21 12:05:15.913137+07:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '985abc5802c1'
down_revision = '25a53e679336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follower_following',
    sa.Column('follower_id', sa.BIGINT(), nullable=False),
    sa.Column('following_id', sa.BIGINT(), nullable=False),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['following_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('follower_id', 'following_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follower_following')
    # ### end Alembic commands ###
