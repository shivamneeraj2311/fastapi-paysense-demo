"""Tables Added with relation

Revision ID: 165b1ab38fd5
Revises: b0fe48885a4a
Create Date: 2023-11-02 16:31:00.290563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '165b1ab38fd5'
down_revision: Union[str, None] = 'b0fe48885a4a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('DummyOrg', sa.Column('dummy_user_id', sa.String(length=32), nullable=False))
    op.create_index(op.f('ix_DummyOrg_dummy_user_id'), 'DummyOrg', ['dummy_user_id'], unique=False)
    op.create_foreign_key(None, 'DummyOrg', 'DummyUser', ['dummy_user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'DummyOrg', type_='foreignkey')
    op.drop_index(op.f('ix_DummyOrg_dummy_user_id'), table_name='DummyOrg')
    op.drop_column('DummyOrg', 'dummy_user_id')
    # ### end Alembic commands ###