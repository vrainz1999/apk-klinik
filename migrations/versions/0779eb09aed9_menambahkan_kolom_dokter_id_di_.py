"""Menambahkan kolom dokter_id di Pendaftaran

Revision ID: 0779eb09aed9
Revises: a96b82be9916
Create Date: 2024-09-17 04:29:52.725708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0779eb09aed9'
down_revision = 'a96b82be9916'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pendaftaran', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dokter_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'dokter', ['dokter_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pendaftaran', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('dokter_id')

    # ### end Alembic commands ###