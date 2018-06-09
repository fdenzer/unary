"""empty message

Revision ID: 5596da4479dc
Revises: 0cb26867ad03
Create Date: 2018-06-09 12:30:48.072183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5596da4479dc'
down_revision = '0cb26867ad03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('description', sa.String(length=500), server_default='', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'description')
    # ### end Alembic commands ###
