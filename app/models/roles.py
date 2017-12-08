from app import db

class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(140))

    peoples = db.relationship('User', backref='role_owner', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % (self.role_name)