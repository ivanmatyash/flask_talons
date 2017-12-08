from app import db
from app.models.mixins import json_creator

class Speciality(json_creator.WithJsonCreate, db.Model):
    __tablename__ = "specialities"
    id = db.Column(db.Integer, primary_key=True)
    speciality_name = db.Column(db.String(140))

    doctors = db.relationship('Doctor', backref='spec_doctor', lazy='dynamic')

    def get_properties(self):
        return [
            "id",
            "speciality_name"
        ]

    def __repr__(self):

        return '<Speciality %r>' % (self.speciality_name)