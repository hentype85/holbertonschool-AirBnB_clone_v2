#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """ returns the list of City instances with state_id 
            equals to the current State.id"""
        list_city = []
        for city in models.storage.all(models.City).values():
            if city.state.id == self.id:
                list_city.append(city)
        return list_city