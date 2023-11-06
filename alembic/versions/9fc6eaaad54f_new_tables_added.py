"""New Tables Added

Revision ID: 9fc6eaaad54f
Revises: 
Create Date: 2023-11-06 16:49:52.043236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fc6eaaad54f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('surname', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_User_id'), 'User', ['id'], unique=False)
    op.create_index(op.f('ix_User_name'), 'User', ['name'], unique=False)
    op.create_index(op.f('ix_User_surname'), 'User', ['surname'], unique=False)
    op.create_table('Org',
    sa.Column('dummy_user_id', sa.Integer(), nullable=True),
    sa.Column('org_name', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['dummy_user_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Org_dummy_user_id'), 'Org', ['dummy_user_id'], unique=False)
    op.create_index(op.f('ix_Org_id'), 'Org', ['id'], unique=False)
    op.create_index(op.f('ix_Org_org_name'), 'Org', ['org_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Org_org_name'), table_name='Org')
    op.drop_index(op.f('ix_Org_id'), table_name='Org')
    op.drop_index(op.f('ix_Org_dummy_user_id'), table_name='Org')
    op.drop_table('Org')
    op.drop_index(op.f('ix_User_surname'), table_name='User')
    op.drop_index(op.f('ix_User_name'), table_name='User')
    op.drop_index(op.f('ix_User_id'), table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###