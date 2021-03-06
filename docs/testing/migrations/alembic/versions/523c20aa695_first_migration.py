"""First Migration

Revision ID: 523c20aa695
Revises:
Create Date: 2015-11-04 12:15:36.577201

"""

# revision identifiers, used by Alembic.
revision = '523c20aa695'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('companies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Unicode(length=200), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table('employees',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.Unicode(length=200), nullable=True),
        sa.Column('age', sa.Integer(), nullable=False),
        sa.Column('ssn', sa.Unicode(length=30), nullable=False),
        sa.Column(
            'favourite_meal',
            sa.Enum('meat', 'vegan', 'vegetarian'),
            nullable=False
        ),
        sa.Column('company_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['company_id'], ['companies.id'], name='fk_employees_companies'
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table('addresses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('address', sa.Unicode(length=200), nullable=True),
        sa.Column('zip_code', sa.Unicode(length=20), nullable=True),
        sa.Column('city', sa.Unicode(length=100), nullable=True),
        sa.Column('country', sa.Unicode(length=3), nullable=True),
        sa.Column('person_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['person_id'], ['employees.id'], name='fk_addresses_employees'
        ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phone_numbers',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('number', sa.String(length=40), nullable=True),
        sa.Column('owner', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['owner'], ['employees.id'], name='fk_phone_numbers_employees'
        ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('phone_numbers')
    op.drop_table('addresses')
    op.drop_table('employees')
    op.drop_table('companies')
