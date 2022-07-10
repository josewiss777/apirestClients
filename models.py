#Register imports
from flask_sqlalchemy import SQLAlchemy

#SQLAlchemy instance
db = SQLAlchemy()

#Register models
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    basic = db.Column(db.String(20), nullable=True)
    full = db.Column(db.String(20), nullable=True)
    date = db.Column(db.String(20), nullable=False)
    def __init__(self, name, phone, email, basic, full, date):
        self.name = name
        self.phone = phone
        self.email = email
        self.basic = basic
        self.full = full
        self.date = date