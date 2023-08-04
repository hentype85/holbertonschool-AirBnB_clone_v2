#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.place import Place
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey(Place.id), nullable=False)
    user_id = Column(String(60), ForeignKey(Place.id), nullable=False)
    text = Column(String(1024), nullable=False)
