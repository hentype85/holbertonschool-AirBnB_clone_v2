#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """initialize attributes"""
        strtimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())

            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, strtimeFormat))
                elif k != "__class__":
                    setattr(self, k, v)

            now = datetime.now()
            if "created_at" not in kwargs:
                self.created_at = now
            if "updated_at" not in kwargs:
                self.updated_at = now
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
