"""empty message

Revision ID: 4a384e785315
Revises: a5cffa318ac2
Create Date: 2024-02-21 10:42:36.709470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a384e785315'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_name', sa.String(length=40), nullable=True),
    sa.Column('climate', sa.String(length=40), nullable=True),
    sa.Column('rotation_period', sa.String(length=40), nullable=True),
    sa.Column('population', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('planet_name')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_name', sa.String(length=40), nullable=True),
    sa.Column('model', sa.String(length=40), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('eye_color', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('homeworld', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['homeworld'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_name', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['planet_name'], ['planet.planet_name'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('firstname', sa.String(length=40), nullable=True))
        batch_op.add_column(sa.Column('lastname', sa.String(length=40), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_firstname'), ['firstname'], unique=False)
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_index(batch_op.f('ix_user_firstname'))
        batch_op.drop_column('lastname')
        batch_op.drop_column('firstname')

    op.drop_table('favorite_planet')
    op.drop_table('character')
    op.drop_table('vehicle')
    op.drop_table('planet')
    # ### end Alembic commands ###