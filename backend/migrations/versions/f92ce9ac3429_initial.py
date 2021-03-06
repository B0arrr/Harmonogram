"""Initial

Revision ID: f92ce9ac3429
Revises: 
Create Date: 2022-04-24 01:48:53.026713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f92ce9ac3429'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employment', sa.String(), nullable=False),
    sa.Column('hours_per_week', sa.Integer(), nullable=True),
    sa.Column('hours_per_day', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employment_employment'), 'employment', ['employment'], unique=False)
    op.create_index(op.f('ix_employment_id'), 'employment', ['id'], unique=False)
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_position_id'), 'position', ['id'], unique=False)
    op.create_index(op.f('ix_position_name'), 'position', ['name'], unique=False)
    op.create_table('schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('day', sa.Date(), nullable=False),
    sa.Column('day_off', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_schedule_day'), 'schedule', ['day'], unique=False)
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('employment_id', sa.Integer(), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employment_id'], ['employment.id'], ),
    sa.ForeignKeyConstraint(['position_id'], ['position.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_email'), 'employee', ['email'], unique=True)
    op.create_index(op.f('ix_employee_id'), 'employee', ['id'], unique=False)
    op.create_index(op.f('ix_employee_login'), 'employee', ['login'], unique=True)
    op.create_index(op.f('ix_employee_name'), 'employee', ['name'], unique=False)
    op.create_index(op.f('ix_employee_surname'), 'employee', ['surname'], unique=False)
    op.create_table('schedule_employee',
    sa.Column('schedule_id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('shift', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employee.id'], ),
    sa.ForeignKeyConstraint(['schedule_id'], ['schedule.id'], ),
    sa.PrimaryKeyConstraint('schedule_id', 'employee_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('schedule_employee')
    op.drop_index(op.f('ix_employee_surname'), table_name='employee')
    op.drop_index(op.f('ix_employee_name'), table_name='employee')
    op.drop_index(op.f('ix_employee_login'), table_name='employee')
    op.drop_index(op.f('ix_employee_id'), table_name='employee')
    op.drop_index(op.f('ix_employee_email'), table_name='employee')
    op.drop_table('employee')
    op.drop_index(op.f('ix_schedule_day'), table_name='schedule')
    op.drop_table('schedule')
    op.drop_index(op.f('ix_position_name'), table_name='position')
    op.drop_index(op.f('ix_position_id'), table_name='position')
    op.drop_table('position')
    op.drop_index(op.f('ix_employment_id'), table_name='employment')
    op.drop_index(op.f('ix_employment_employment'), table_name='employment')
    op.drop_table('employment')
    # ### end Alembic commands ###
