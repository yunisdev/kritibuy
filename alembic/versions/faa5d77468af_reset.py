"""reset

Revision ID: faa5d77468af
Revises: c3445ad0d56b
Create Date: 2020-11-28 18:28:06.513057

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'faa5d77468af'
down_revision = 'c3445ad0d56b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Countries',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('alpha2', sa.String(length=5), nullable=False),
    sa.Column('alpha3', sa.String(length=5), nullable=False),
    sa.Column('flagPath', sa.String(), nullable=False),
    sa.Column('phonePrefix', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('CouponCodes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('usable', sa.Integer(), nullable=False),
    sa.Column('used', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Permissions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ServerErrors',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('where', sa.String(), nullable=False),
    sa.Column('errorCode', sa.Integer(), nullable=False),
    sa.Column('errorDesc', sa.String(), nullable=False),
    sa.Column('fixed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Cities',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('country', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country'], ['Countries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('permission', sa.Integer(), nullable=False),
    sa.Column('fullName', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('country', sa.Integer(), nullable=False),
    sa.Column('city', sa.Integer(), nullable=False),
    sa.Column('brandLogoPath', sa.String(), nullable=True),
    sa.Column('brandName', sa.String(), nullable=True),
    sa.Column('brandNameSynonyms', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('brandProductTypes', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('confirmationKey', sa.String(), nullable=False),
    sa.Column('confirmed', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['Cities.id'], ),
    sa.ForeignKeyConstraint(['country'], ['Countries.id'], ),
    sa.ForeignKeyConstraint(['permission'], ['Permissions.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('brandName'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('AuthTokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Messages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=4), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Orders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('orderedTo', sa.Integer(), nullable=False),
    sa.Column('orderedBy', sa.Integer(), nullable=False),
    sa.Column('orderedProduct', sa.String(), nullable=False),
    sa.Column('orderText', sa.String(), nullable=False),
    sa.Column('comments', sa.String(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['orderedBy'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['orderedTo'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('PasswordRecover',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Payments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('fromUser', sa.Integer(), nullable=False),
    sa.Column('toUser', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['fromUser'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['toUser'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Reports',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('reporter', sa.Integer(), nullable=False),
    sa.Column('header', sa.String(), nullable=False),
    sa.Column('body', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['reporter'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Wallets',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('owner')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Wallets')
    op.drop_table('Reports')
    op.drop_table('Payments')
    op.drop_table('PasswordRecover')
    op.drop_table('Orders')
    op.drop_table('Messages')
    op.drop_table('AuthTokens')
    op.drop_table('Users')
    op.drop_table('Cities')
    op.drop_table('ServerErrors')
    op.drop_table('Permissions')
    op.drop_table('CouponCodes')
    op.drop_table('Countries')
    # ### end Alembic commands ###