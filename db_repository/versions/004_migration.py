from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
week_timetable = Table('week_timetable', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('doctor_id', Integer, nullable=False),
    Column('monday', String(length=120), default=ColumnDefault('10:00 - 15:00')),
    Column('tuesday', String(length=120), default=ColumnDefault('10:00 - 15:00')),
    Column('wednesday', String(length=120), default=ColumnDefault('10:00 - 15:00')),
    Column('thursday', String(length=120), default=ColumnDefault('10:00 - 15:00')),
    Column('friday', String(length=120), default=ColumnDefault('10:00 - 15:00')),
    Column('saturday', String(length=120), default=ColumnDefault('11:00 - 13:00')),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['week_timetable'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['week_timetable'].drop()
