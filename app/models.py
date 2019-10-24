from flask_login import UserMixin
from .webserver import initdb as db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    fname = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    uname = db.Column(db.String(1000))
    role = db.Column(db.Integer)