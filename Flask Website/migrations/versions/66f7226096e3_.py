"""empty message

Revision ID: 66f7226096e3
Revises: 4b356b86b11a
Create Date: 2022-07-12 12:14:39.840836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66f7226096e3'
down_revision = '4b356b86b11a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'blogpost')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('blogpost', sa.VARCHAR(length=180), nullable=True))
    # ### end Alembic commands ###
