"""empty message

Revision ID: ac8bd1071bb4
Revises: 271520156ed4
Create Date: 2021-05-13 10:11:49.495740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac8bd1071bb4'
down_revision = '271520156ed4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fiats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fiats')
    # ### end Alembic commands ###
