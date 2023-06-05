"""Changing column name from name to nickname

Revision ID: b107c018c909
Revises: 791279dd0760
Create Date: 2023-06-05 05:38:27.807934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b107c018c909'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='nickname')


def downgrade() -> None:
    op.alter_column('students', 'nickname', new_column_name='name')
