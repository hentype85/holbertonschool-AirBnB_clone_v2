#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from sqlalchemy.orm import relationship
from sqlalchemy import *
import models


place_amenity = Table(
    "place_amenity", Base.metadata,
    Column("place_id", String(60), ForeignKey(Place.id),
           primary_key=True, nullable=False),
    Column("amenity_id", String(60), ForeignKey(Amenity.id),
           primary_key=True, nullable=False)
    )


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

    @property
    def reviews(self):
        """ returns the list of Review instances
            with place_id equals to the current Place.id"""
        list_review = []
        for review in models.storage.all(models.Review).values():
            if review.place_id == self.id:
                list_review.append(review)
        return list_review
