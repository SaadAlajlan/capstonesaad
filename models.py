
import os
from sqlalchemy import Column, String, Integer , create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_path = """postgres://abyprsksvzqemp:6d884d9f58a50090d22ff74893b4b401b0ab4504d2431b0b399ca9a6e37ed0f6@ec2-54-234-28-165.compute-1.amazonaws.com:5432/dbaq9joi9ijb85"""

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


class Coffeeshops(db.Model):
    __tablename__ = "coffeeshop"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    rate = Column(String)
    recommended = Column(String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'rate': self.rate,
            'recommended': self.recommended
        }


class Visited(db.Model):
    __tablename__ = "visited"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    recommended = Column(String)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return{
            'id': self.id,
            'name': self.name,
            'recommended': self.recommended
        }