from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
doctors = Table('doctors', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=120)),
    Column('photo_url', String(length=120)),
    Column('speciality_id', Integer, nullable=False),
)

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

polyclinics = Table('polyclinics', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('polyclinic_number', Integer),
    Column('address', String(length=140)),
)

roles = Table('roles', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('role_name', String(length=140)),
)

specialities = Table('specialities', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('speciality_name', String(length=140)),
)

timetables = Table('timetables', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('doctor_id', Integer, nullable=False),
    Column('polyclinic_id', Integer, nullable=False),
    Column('patient_id', Integer),
    Column('time', DateTime),
    Column('room_number', String(length=10)),
    Column('departure', Boolean, default=ColumnDefault(False)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['doctors'].create()
    post_meta.tables['people'].create()
    post_meta.tables['polyclinics'].create()
    post_meta.tables['roles'].create()
    post_meta.tables['specialities'].create()
    post_meta.tables['timetables'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['doctors'].drop()
    post_meta.tables['people'].drop()
    post_meta.tables['polyclinics'].drop()
    post_meta.tables['roles'].drop()
    post_meta.tables['specialities'].drop()
    post_meta.tables['timetables'].drop()
