""" Renaming students to sscholar

Revision ID: 30ba632ef55c
Revises: 791279dd0760
Create Date: 2023-12-13 14:51:24.918982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30ba632ef55c'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
