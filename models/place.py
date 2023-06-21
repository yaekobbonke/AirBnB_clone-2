#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models import base_model
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, metadata, Integer, Float

Base = declarative_base()


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), foreignKey('cities.id'))
    user_id = Column(String(60), foreignKey('users.id'))
    name = Column(String(128))
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)


Base.metadata.create_all(engine)
