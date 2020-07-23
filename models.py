
import os
from sqlalchemy import Column, String, Integer , create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_path = """postgres://fuslttnjinadwk:df83c0b314934b2f64e6de8ec6f5730f7e3fb39da0d3c7fc83165c20d8ab3c76@ec2-3-215-83-17.compute-1.amazonaws.com:5432/ddevls1ouhbli0"""

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()



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