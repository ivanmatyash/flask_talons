from app import db
from app.models.mixins import json_creator

class Role(json_creator.WithJsonCreate, db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(140))

    peoples = db.relationship('User', backref='role_owner', lazy='dynamic')

    def get_properties(self):
        return [
            "id",
            "role_name"
        ]

    def __repr__(self):
        return '<Role %r>' % (self.role_name)