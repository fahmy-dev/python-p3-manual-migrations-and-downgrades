"""Renaming students to scholars

Revision ID: 20287e90bf31
Revises: 791279dd0760
Create Date: 2025-03-10 00:02:13.867257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20287e90bf31'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
