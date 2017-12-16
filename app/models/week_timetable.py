from app import db
from app.models.mixins import json_creator
from sqlalchemy.ext.hybrid import hybrid_property

class WeekTimetable(json_creator.WithJsonCreate, db.Model):
    __tablename__ = "week_timetable"
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    doctor = db.relationship("Doctor")
    monday = db.Column(db.String(120), default="10:00 - 15:00")
    tuesday = db.Column(db.String(120), default="10:00 - 15:00")
    wednesday = db.Column(db.String(120), default="10:00 - 15:00")
    thursday = db.Column(db.String(120), default="10:00 - 15:00")
    friday = db.Column(db.String(120), default="10:00 - 15:00")
    saturday = db.Column(db.String(120), default="11:00 - 13:00")

    @hybrid_property
    def doctor_name(self):
        return self.doctor.name

    @hybrid_property
    def speciality_id(self):
        return self.doctor.speciality.id

    @hybrid_property
    def speciality_name(self):
        return self.doctor.speciality.speciality_name


    def get_properties(self):
        return [
            "id",
            "doctor_id",
            "doctor_name",
            "speciality_id",
            "speciality_name",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday"
        ]