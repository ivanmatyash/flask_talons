from app import db
from app.models.mixins import json_creator
from sqlalchemy.ext.hybrid import hybrid_property

class Doctor(json_creator.WithJsonCreate, db.Model):
    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    photo_url = db.Column(db.String(120))
    speciality_id = db.Column(db.Integer, db.ForeignKey('specialities.id'), nullable=False)
    speciality = db.relationship("Speciality")

    timetables = db.relationship('Timetable', backref='priem', lazy='dynamic')

    @hybrid_property
    def speciality_name(self):
        return self.speciality.speciality_name

    def get_properties(self):
        return [
            "id",
            "name",
            "photo_url",
            "speciality_id",
            "speciality_name"
        ]

    def __repr__(self):
        return '<Doctor %r>' % (self.name)