import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

base_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Person(db.Model):

    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"id = {self.id}, name={self.name}, age={self.age}"

