"""User table

Revision ID: 1f1e70e3c7d5
Revises: 
Create Date: 2020-04-20 19:39:35.853482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f1e70e3c7d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('sector', sa.String(length=64), nullable=True),
    sa.Column('subcategory', sa.String(length=64), nullable=True),
    sa.Column('resumelink', sa.String(length=400), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_firstname'), 'user', ['firstname'], unique=True)
    op.create_index(op.f('ix_user_lastname'), 'user', ['lastname'], unique=True)
    op.create_index(op.f('ix_user_resumelink'), 'user', ['resumelink'], unique=True)
    op.create_index(op.f('ix_user_sector'), 'user', ['sector'], unique=True)
    op.create_index(op.f('ix_user_subcategory'), 'user', ['subcategory'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_subcategory'), table_name='user')
    op.drop_index(op.f('ix_user_sector'), table_name='user')
    op.drop_index(op.f('ix_user_resumelink'), table_name='user')
    op.drop_index(op.f('ix_user_lastname'), table_name='user')
    op.drop_index(op.f('ix_user_firstname'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
