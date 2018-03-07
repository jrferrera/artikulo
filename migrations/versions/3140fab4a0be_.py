"""empty message

Revision ID: 3140fab4a0be
Revises: 713cd7fc65e2
Create Date: 2018-03-07 14:57:52.558808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3140fab4a0be'
down_revision = '713cd7fc65e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=255), nullable=False))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
