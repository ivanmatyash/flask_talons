from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
doctors = Table('doctors', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('user_id', INTEGER, nullable=False),
    Column('speciality_id', INTEGER, nullable=False),
)

doctors = Table('doctors', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=120)),
    Column('photo_url', String(length=120)),
    Column('speciality_id', Integer, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['doctors'].columns['user_id'].drop()
    post_meta.tables['doctors'].columns['name'].create()
    post_meta.tables['doctors'].columns['photo_url'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['doctors'].columns['user_id'].create()
    post_meta.tables['doctors'].columns['name'].drop()
    post_meta.tables['doctors'].columns['photo_url'].drop()
