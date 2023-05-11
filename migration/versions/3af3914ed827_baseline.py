"""baseline

Revision ID: 3af3914ed827
Revises: 
Create Date: 2023-05-11 23:29:05.521307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3af3914ed827'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'customer',
        column=sa.Column('personal_discount', sa.types.Integer)
    )
    op.alter_column(
        'product',
        column_name='price',
        type_=sa.types.Float
    )


def downgrade() -> None:
    pass
