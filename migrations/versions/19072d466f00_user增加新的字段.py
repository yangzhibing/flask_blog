"""'User增加新的字段'

Revision ID: 19072d466f00
Revises: 90f704ea7ce7
Create Date: 2019-07-22 15:47:27.404226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19072d466f00'
down_revision = '90f704ea7ce7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
