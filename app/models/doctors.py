from app import db

class Doctor(db.Model):
    __tablename__ = "doctors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    photo_url = db.Column(db.String(120))
    speciality_id = db.Column(db.Integer, db.ForeignKey('specialities.id'), nullable=False)
    speciality = db.relationship("Speciality")

    timetables = db.relationship('Timetable', backref='priem', lazy='dynamic')

    def __repr__(self):
        return '<Doctor %r>' % (self.name)