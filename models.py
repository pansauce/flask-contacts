from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Contact(db.Model):

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), nullable=False)
    lname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(200), nullable=True, unique=False)
    phone = db.Column(db.String(20), nullable=True, unique=False)
    title = db.Column(db.String(50), nullable=True, unique=False)
    company = db.Column(db.String(100), nullable=True, unique=False)

    def __repr__(self):
        return "[0]"
