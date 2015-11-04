"""Initial Migration

Revision ID: 4f8bcaa1a66
Revises:
Create Date: 2015-11-04 11:01:47.525299

"""

# revision identifiers, used by Alembic.
revision = '4f8bcaa1a66'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.create_table('companies',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Unicode(length=200), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    op.create_table('employees',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Unicode(length=200), nullable=True),
        sa.Column('age', sa.Integer(), nullable=False),
        sa.Column('ssn', sa.Unicode(length=30), nullable=False),
        sa.Column(
            'favourite_meal', sa.Enum('meat', 'vegetarian'), nullable=False),
        sa.Column('company_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['company_id'], ['companies.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        op.f('ix_employees_name'), 'employees', ['name'], unique=True)

    op.create_table('addresses',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('address', sa.Unicode(length=200), nullable=True),
        sa.Column('zip_code', sa.Unicode(length=20), nullable=True),
        sa.Column('city', sa.Unicode(length=100), nullable=True),
        sa.Column('country', sa.Unicode(length=3), nullable=True),
        sa.Column('person_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['person_id'], ['employees.id']),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('phone_numbers',
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('number', sa.String(length=40), nullable=False),
        sa.Column('owner', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['owner'], ['employees.id']),
        sa.PrimaryKeyConstraint('id')
    )



def downgrade():
    op.drop_table('phone_numbers')
    op.drop_table('addresses')
    op.drop_index(op.f('ix_employees_name'), table_name='employees')
    op.drop_table('employees')
    op.drop_table('companies')
