from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
doctors = Table('doctors', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer, nullable=False),
    Column('speciality_id', Integer, nullable=False),
)

specialities = Table('specialities', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('speciality_name', String(length=140)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['doctors'].create()
    post_meta.tables['specialities'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['doctors'].drop()
    post_meta.tables['specialities'].drop()
