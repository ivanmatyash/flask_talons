from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
roles = Table('roles', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('role_name', VARCHAR(length=140)),
)

people = Table('people', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=120), nullable=False),
    Column('password', VARCHAR(length=120), nullable=False),
    Column('name', VARCHAR(length=120)),
    Column('birthday', DATE),
    Column('role_id', INTEGER, nullable=False),
    Column('photo_url', VARCHAR(length=120)),
    Column('parent_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['roles'].drop()
    pre_meta.tables['people'].columns['role_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['roles'].create()
    pre_meta.tables['people'].columns['role_id'].create()
