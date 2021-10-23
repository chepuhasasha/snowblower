# coding: utf-8
from datetime import datetime

# from sqlalchemy.orm import backref
from src import db
from sqlalchemy.dialects import postgresql

# # {
# #     "id": 1,
# #     "name": "Бульдозер максим",
# #     "number": "АУ777Е",
# #     "status": "В работе",
# #     "coords": [52.60283902179348, 39.5168277094808],
# #     "way": [
# #         [52.594706282077965, 39.50395579982881],
# #         [52.609198189273584, 39.5296996191328],
# #         [52.605758098557764, 39.53278887744928],
# #         [52.60409007851464, 39.53793764131006]
# #     ]
# # }


class Base:
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Venicle(db.Model, Base):
    __tablename__ = 'venicle'

    id = db.Column(db.Integer, primary_key=True,
                   index=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, index=True, nullable=False)
    number = db.Column(db.String(10), nullable=False)
    coord = db.Column(postgresql.ARRAY(db.Float))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Task(db.Model, Base):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True,
                   index=True, autoincrement=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)
    distance = db.Column(db.Integer, default=0)
    venicle_id = db.Column(db.Integer, db.ForeignKey('venicle.id'))
    routes = db.relationship('Route', backref='task', lazy=True)


class Route(db.Model, Base):
    __tablename__ = 'route'

    id = db.Column(db.Integer, primary_key=True,
                   index=True, autoincrement=True)
    coord = db.Column(postgresql.ARRAY(db.Float))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'),
                        nullable=False)
