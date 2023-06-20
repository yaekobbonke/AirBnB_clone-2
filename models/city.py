#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Culumn


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    name = Column(String(128), NOT None),
    state_id = Column(String(60), forein_key(states.id))
