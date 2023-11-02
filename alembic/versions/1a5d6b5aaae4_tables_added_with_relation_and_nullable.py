"""Tables Added with relation and nullable

Revision ID: 1a5d6b5aaae4
Revises: 165b1ab38fd5
Create Date: 2023-11-02 16:33:22.303290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a5d6b5aaae4'
down_revision: Union[str, None] = '165b1ab38fd5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('DummyOrg', 'dummy_user_id',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('DummyOrg', 'dummy_user_id',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)
    # ### end Alembic commands ###
