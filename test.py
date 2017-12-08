import subprocess
import datetime
from app import db, models

subprocess.call(['./db_reset'])

sp = models.Speciality(speciality_name="terapevt")
db.session.add(sp)
db.session.commit()

doctor = models.Doctor(name="Ivan", speciality=sp)
db.session.add(doctor)
db.session.commit()

polyclinic = models.Polyclinic(polyclinic_number=5, address="Minsk, Oktybrskaya 10")



r1 = models.Role(role_name="patient")
db.session.add(r1)
db.session.commit()

patient = models.User(name="bol", email="test1@3a.by", password="123456", role=r1, parent_id=1)
db.session.add(patient)
db.session.commit()

record = models.Timetable(doctor=doctor, polyclinic=polyclinic, patient=patient, time=datetime.datetime.now(), room_number="1234")

print record