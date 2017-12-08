from app import db

class Polyclinic(db.Model):
    __tablename__ = "polyclinics"
    id = db.Column(db.Integer, primary_key=True)
    polyclinic_number = db.Column(db.Integer)
    address = db.Column(db.String(140))

    timetables = db.relationship('Timetable', backref='priem_pol', lazy='dynamic')

    def __repr__(self):
        return '<Polyclinic %r>' % (self.polyclinic_number)