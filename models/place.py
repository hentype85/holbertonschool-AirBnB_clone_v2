#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms =  Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
