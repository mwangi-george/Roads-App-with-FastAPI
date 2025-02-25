"""Migrating to SQLite DB

Revision ID: 17ecd5ca7181
Revises: 
Create Date: 2024-07-13 18:18:11.897404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17ecd5ca7181'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
                    sa.Column('location_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('latitude', sa.Float(), nullable=True),
                    sa.Column('longitude', sa.Float(), nullable=True),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('location_id')
                    )
    op.create_index(op.f('ix_locations_location_id'),
                    'locations', ['location_id'], unique=False)
    op.create_table('roads',
                    sa.Column('road_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('length_km', sa.Float(), nullable=True),
                    sa.Column('construction_year',
                              sa.Integer(), nullable=True),
                    sa.Column('start_location_id',
                              sa.Integer(), nullable=False),
                    sa.Column('end_location_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['end_location_id'], [
                        'locations.location_id'], ),
                    sa.ForeignKeyConstraint(['start_location_id'], [
                        'locations.location_id'], ),
                    sa.PrimaryKeyConstraint('road_id')
                    )
    op.create_index(op.f('ix_roads_construction_year'),
                    'roads', ['construction_year'], unique=False)
    op.create_index(op.f('ix_roads_name'), 'roads', ['name'], unique=False)
    op.create_index(op.f('ix_roads_road_id'), 'roads',
                    ['road_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roads_road_id'), table_name='roads')
    op.drop_index(op.f('ix_roads_name'), table_name='roads')
    op.drop_index(op.f('ix_roads_construction_year'), table_name='roads')
    op.drop_table('roads')
    op.drop_index(op.f('ix_locations_location_id'), table_name='locations')
    op.drop_table('locations')
    # ### end Alembic commands ###
