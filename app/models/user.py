from app import db
from app.models.mixins import json_creator
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext.login import UserMixin
from app.login_manager import login_manager

class User(json_creator.WithJsonCreate, db.Model, UserMixin):
    __tablename__ = "people"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(120), index=True, unique=False, nullable=False)
    name = db.Column(db.String(120), index=True, unique=False)
    birthday = db.Column(db.Date)
    photo_url = db.Column(db.String(120))
    parent_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    children = db.relationship("User")
    parent = db.relationship("User", remote_side=[id])
    timetables = db.relationship('Timetable', backref='priem_user', lazy='dynamic')

    @login_manager.user_loader
    def load_user(userid):
        return User.query.get(userid)

    def get_properties(self):
        return [
            "id",
            "name",
            "email",
            "birthday",
            "photo_url",
            "parent_id",
        ]


    def __repr__(self):
        return '<User %r>' % (self.name)