from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/contact_management"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class ContactCardModel(db.Model):
    __tablename__ = 'contact_cards'

    case_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    mobile_number = db.Column(db.Integer())
    address = db.Column(db.String())

    def __init__(self, case_id, title, first_name, last_name, mobile_number, address):
        self.case_id = case_id
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.address = address

    def __repr__(self):
        return f"<Contact card {self.name}>"