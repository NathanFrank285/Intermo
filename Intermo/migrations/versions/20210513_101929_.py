"""empty message

Revision ID: 69dc5aef7045
Revises: ac8bd1071bb4
Create Date: 2021-05-13 10:19:29.807604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69dc5aef7045'
down_revision = 'ac8bd1071bb4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('userBalances_currencyId_fkey', 'userBalances', type_='foreignkey')
    op.create_foreign_key(None, 'userBalances', 'fiats', ['currencyId'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'userBalances', type_='foreignkey')
    op.create_foreign_key('userBalances_currencyId_fkey', 'userBalances', 'currencies', ['currencyId'], ['id'])
    # ### end Alembic commands ###
