from app import db

class User(db.Model):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(120), index=True, unique=False, nullable=False)
    name = db.Column(db.String(120), index=True, unique=False)
    birthday = db.Column(db.Date)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship("Role")
    photo_url = db.Column(db.String(120))

    parent_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    children = db.relationship("User")
    parent = db.relationship("User", remote_side=[id])
    timetables = db.relationship('Timetable', backref='priem_user', lazy='dynamic')
    def __repr__(self):
        return '<User %r>' % (self.name)