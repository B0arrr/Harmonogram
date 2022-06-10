"""rev2

Revision ID: eb0a2ca1c432
Revises: dd5da92a9c3d
Create Date: 2022-06-10 20:43:32.759569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb0a2ca1c432'
down_revision = 'dd5da92a9c3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('department', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'department')
    # ### end Alembic commands ###
