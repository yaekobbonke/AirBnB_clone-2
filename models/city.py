#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Culumn, metadata, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = Column(String(128))
    state_id = Column(String(60), ForeinKey('states.id'))
    places = relationship(Place, backref='City', cascade='delete')
