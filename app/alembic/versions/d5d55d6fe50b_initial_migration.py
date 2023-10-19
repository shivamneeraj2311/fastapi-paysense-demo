"""initial migration

Revision ID: d5d55d6fe50b
Revises: ede002b12124
Create Date: 2023-10-19 12:09:59.054330

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd5d55d6fe50b'
down_revision: Union[str, None] = 'ede002b12124'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dummyuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dummy_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dummyuser_dummy_name'), 'dummyuser', ['dummy_name'], unique=False)
    op.create_index(op.f('ix_dummyuser_id'), 'dummyuser', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dummyuser_id'), table_name='dummyuser')
    op.drop_index(op.f('ix_dummyuser_dummy_name'), table_name='dummyuser')
    op.drop_table('dummyuser')
    # ### end Alembic commands ###