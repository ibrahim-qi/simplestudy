from app import db
from flask_login import UserMixin

# User Model
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True) # each username is unique
    password = db.Column(db.String(32))
    sets = db.relationship('Set', backref='user', lazy='dynamic') # one to many relationship user to sets

    def __repr__(self):
        return '<User %r>' % self.username




