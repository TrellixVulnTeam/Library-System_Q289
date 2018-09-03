"""empty message

Revision ID: 609f22b0ea16
Revises: 620cdbefb4ad
Create Date: 2018-08-16 18:54:42.576873

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '609f22b0ea16'
down_revision = '620cdbefb4ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('memberRequest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('isbn', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userAccount',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_userAccount_email'), 'userAccount', ['email'], unique=True)
    op.create_index(op.f('ix_userAccount_first_name'), 'userAccount', ['first_name'], unique=False)
    op.create_index(op.f('ix_userAccount_last_name'), 'userAccount', ['last_name'], unique=False)
    op.create_index(op.f('ix_userAccount_username'), 'userAccount', ['username'], unique=True)
    op.drop_index('ix_userAccount_email', table_name='useraccount')
    op.drop_index('ix_userAccount_first_name', table_name='useraccount')
    op.drop_index('ix_userAccount_last_name', table_name='useraccount')
    op.drop_index('ix_userAccount_username', table_name='useraccount')
    op.drop_table('useraccount')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('useraccount',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('first_name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_userAccount_username', 'useraccount', ['username'], unique=True)
    op.create_index('ix_userAccount_last_name', 'useraccount', ['last_name'], unique=False)
    op.create_index('ix_userAccount_first_name', 'useraccount', ['first_name'], unique=False)
    op.create_index('ix_userAccount_email', 'useraccount', ['email'], unique=True)
    op.drop_index(op.f('ix_userAccount_username'), table_name='userAccount')
    op.drop_index(op.f('ix_userAccount_last_name'), table_name='userAccount')
    op.drop_index(op.f('ix_userAccount_first_name'), table_name='userAccount')
    op.drop_index(op.f('ix_userAccount_email'), table_name='userAccount')
    op.drop_table('userAccount')
    op.drop_table('memberRequest')
    op.drop_table('books')
    # ### end Alembic commands ###
