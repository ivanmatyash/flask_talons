from app import db
from app.models.mixins import json_creator
from sqlalchemy.ext.hybrid import hybrid_property

class Timetable(json_creator.WithJsonCreate, db.Model):
    __tablename__ = "timetables"
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    doctor = db.relationship("Doctor")

    polyclinic_id = db.Column(db.Integer, db.ForeignKey('polyclinics.id'), nullable=False)
    polyclinic = db.relationship("Polyclinic")

    patient_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    patient = db.relationship("User")

    time = db.Column(db.DateTime)
    room_number = db.Column(db.String(10))

    departure = db.Column(db.Boolean, default=False)

    @hybrid_property
    def doctor_name(self):
        return self.doctor.name
    @hybrid_property
    def doctor_speciality(self):
        return self.doctor.speciality_name

    @hybrid_property
    def polyclinic_number(self):
        return self.polyclinic.polyclinic_number

    @hybrid_property
    def polyclinic_address(self):
        return self.polyclinic.address

    @hybrid_property
    def patient_name(self):
        return self.patient.name

    @hybrid_property
    def patient_birthday(self):
        return self.patient.birthday

    @hybrid_property
    def patient_photo_url(self):
        return self.patient.photo_url

    @hybrid_property
    def doctor_photo_url(self):
        return self.doctor.photo_url

    def get_properties(self):
        return [
            "id",
            "doctor_id",
            "doctor_name",
            "doctor_speciality",
            "polyclinic_id",
            "polyclinic_number",
            "polyclinic_address",
            "patient_id",
            "patient_name",
            "patient_birthday",
            "patient_photo_url",
            "doctor_photo_url",
            "time",
            "room_number",
            "departure"
        ]

    def __repr__(self):
        return '<Timetable. Doctor = {0}, polyclinic = {1}, patient = {2}, time = {3}, room = {4}>'.format(self.doctor,
                                                                                                           self.polyclinic,
                                                                                                           self.patient,
                                                                                                           self.time,
                                                                                                           self.room_number)