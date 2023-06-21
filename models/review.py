#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    text = Column(String(1024))
    place_id = Column(String(60), ForeignKey('places.id'))
    user_id = Column(String(60), ForeignKey('users.id'))
