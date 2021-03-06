"""empty message

Revision ID: e70d6f69d510
Revises: 98c50feda702
Create Date: 2022-02-22 16:25:35.811339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e70d6f69d510'
down_revision = '98c50feda702'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todolist', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolist')
    # ### end Alembic commands ###
