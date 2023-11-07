"""empty message

Revision ID: 64e5bb84839a
Revises: 7ed78bbf0e74
Create Date: 2023-11-03 12:31:30.847814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64e5bb84839a'
down_revision = '7ed78bbf0e74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stocks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('behavior', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stocks', schema=None) as batch_op:
        batch_op.drop_column('behavior')

    # ### end Alembic commands ###