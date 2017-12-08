from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
people = Table('people', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('email', String(length=120), nullable=False),
    Column('password', String(length=120), nullable=False),
    Column('name', String(length=120)),
    Column('birthday', Date),
    Column('role_id', Integer, nullable=False),
    Column('photo_url', String(length=120)),
    Column('parent_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['people'].columns['parent_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['people'].columns['parent_id'].drop()
