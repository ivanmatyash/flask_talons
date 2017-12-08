from app import db

class Speciality(db.Model):
    __tablename__ = "specialities"
    id = db.Column(db.Integer, primary_key=True)
    speciality_name = db.Column(db.String(140))

    doctors = db.relationship('Doctor', backref='spec_doctor', lazy='dynamic')

    def __repr__(self):
        return '<Speciality %r>' % (self.speciality_name)