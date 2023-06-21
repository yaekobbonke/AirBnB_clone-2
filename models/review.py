#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Colum, String, metadata
from models import base_model

Base = declarative_base()


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    text = Column(String(1024))
    place_id = Column(String(60), foreignKey('places.id'))
    user_id = Column(String(60), foreignKey('users.id'))

Base.metadata.create_all()
