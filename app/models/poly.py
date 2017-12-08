from app import db
from app.models.mixins import json_creator

class Polyclinic(json_creator.WithJsonCreate, db.Model):
    __tablename__ = "polyclinics"
    id = db.Column(db.Integer, primary_key=True)
    polyclinic_number = db.Column(db.Integer)
    address = db.Column(db.String(140))

    timetables = db.relationship('Timetable', backref='priem_pol', lazy='dynamic')

    def get_properties(self):
        return [
            "id",
            "polyclinic_number",
            "address"
        ]

    def __repr__(self):
        return '<Polyclinic %r>' % (self.polyclinic_number)