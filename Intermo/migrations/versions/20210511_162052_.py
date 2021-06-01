"""empty message

Revision ID: 28b2ea2a81fe
Revises: ffdc0a98111c
Create Date: 2021-05-11 16:20:52.511527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28b2ea2a81fe'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=15), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('postedCurrencyId', sa.Integer(), nullable=False),
    sa.Column('wantedCurrencyId', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(precision=6), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('bidOrOffer', sa.String(length=5), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['postedCurrencyId'], ['currencies.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['wantedCurrencyId'], ['currencies.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('userId', 'postedCurrencyId', 'wantedCurrencyId', 'price', 'bidOrOffer', 'created_on', 'updated_on', 'quantity', name='unique_post')
    )
    op.create_table('userBalances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('currencyId', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['currencyId'], ['currencies.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('makerId', sa.Integer(), nullable=False),
    sa.Column('takerId', sa.Integer(), nullable=False),
    sa.Column('makerCurrencyId', sa.Integer(), nullable=False),
    sa.Column('takerCurrencyId', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('bidOrOffer', sa.String(length=5), nullable=False),
    sa.Column('price', sa.Float(precision=6), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['makerCurrencyId'], ['currencies.id'], ),
    sa.ForeignKeyConstraint(['makerId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['postId'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['takerCurrencyId'], ['currencies.id'], ),
    sa.ForeignKeyConstraint(['takerId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('makerId', 'takerId', 'makerCurrencyId', 'takerCurrencyId', 'quantity', 'bidOrOffer', 'price', 'created_on', name='unique_trade'),
    sa.UniqueConstraint('postId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trades')
    op.drop_table('userBalances')
    op.drop_table('posts')
    op.drop_table('currencies')
    # ### end Alembic commands ###
