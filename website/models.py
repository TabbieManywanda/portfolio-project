from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    bmi = db.relationship('Bmi')
    mealplan_id = db.Column(db.Integer, db.ForeignKey('mealplan.id'))

class Bmi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer)
    height = db.Column(db.Integer)
    age = db.Column(db.Integer)
    whh = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Mealplan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    breakfast = db.Column(db.String(1000))
    snack1 = db.Column(db.String(1000))
    lunch = db.Column(db.String(1000))
    snack2 = db.Column(db.String(1000))
    supper = db.Column(db.String(1000))
    user = db.relationship('User')
