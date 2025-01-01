"""Initial migration.

Revision ID: 0a3fcfbb8bb2
Revises: 
Create Date: 2024-10-03 16:13:05.221565

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0a3fcfbb8bb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('competitions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cName', sa.String(length=100), nullable=False),
    sa.Column('cTime', sa.DateTime(), nullable=False),
    sa.Column('cType', sa.String(length=50), nullable=False),
    sa.Column('Place', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachinfos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tName', sa.String(length=100), nullable=False),
    sa.Column('tType', sa.String(length=50), nullable=False),
    sa.Column('tContact', sa.String(length=100), nullable=False),
    sa.Column('tResume', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Name', sa.String(length=100), nullable=False),
    sa.Column('Password', sa.String(length=100), nullable=False),
    sa.Column('Account', sa.String(length=100), nullable=False),
    sa.Column('Level', sa.String(length=50), nullable=False),
    sa.Column('Mail', sa.String(length=100), nullable=False),
    sa.Column('Phone', sa.String(length=20), nullable=False),
    sa.Column('Age', sa.Integer(), nullable=False),
    sa.Column('Gender', sa.String(length=10), nullable=False),
    sa.Column('Birthday', sa.Date(), nullable=False),
    sa.Column('Dance_age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('videos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('Score', sa.Float(), nullable=False),
    sa.Column('vTime', sa.DateTime(), nullable=False),
    sa.Column('Style', sa.String(length=50), nullable=False),
    sa.Column('Introduction', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('Account')

    op.drop_table('user')
    op.drop_table('video')
    op.drop_table('competition')
    op.drop_table('teachinfo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachinfo',
    sa.Column('tId', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('tName', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('tType', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('tContact', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('tResume', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('tId'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('competition',
    sa.Column('cId', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('cName', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('cTime', mysql.DATETIME(), nullable=True),
    sa.Column('cType', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Place', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('cId'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('video',
    sa.Column('vId', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('Score', mysql.DECIMAL(precision=3, scale=2), nullable=True),
    sa.Column('vTime', mysql.DECIMAL(precision=5, scale=2), nullable=True),
    sa.Column('Style', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Introduction', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('vId'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('user',
    sa.Column('Id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('Name', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('Password', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('Account', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('Level', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('Mail', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Phone', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('Age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('Gender', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('Birthday', sa.DATE(), nullable=True),
    sa.Column('Dance_age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('Account', ['Account'], unique=True)

    op.drop_table('videos')
    op.drop_table('users')
    op.drop_table('teachinfos')
    op.drop_table('competitions')
    # ### end Alembic commands ###
