from app import db

class Timetable(db.Model):
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
    def __repr__(self):
        return '<Timetable. Doctor = {0}, polyclinic = {1}, patient = {2}, time = {3}, room = {4}>'.format(self.doctor,
                                                                                                           self.polyclinic,
                                                                                                           self.patient,
                                                                                                           self.time,
                                                                                                           self.room_number)