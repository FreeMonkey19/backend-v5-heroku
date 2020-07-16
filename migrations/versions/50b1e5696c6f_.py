"""empty message

Revision ID: 50b1e5696c6f
Revises: f0e887bc7edc
Create Date: 2020-07-14 19:42:49.093604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50b1e5696c6f'
down_revision = 'f0e887bc7edc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('site_users', sa.Column('email', sa.String(length=75), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('site_users', 'email')
    # ### end Alembic commands ###
