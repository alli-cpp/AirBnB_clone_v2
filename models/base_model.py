#!/usr/bin/python3
"""
A module that has a base class
defining all classes
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """BaseModel class for all other classes

    Args:
        args (str): arguments
        kwargs (str): keyword arguments

    Attributes:
        id (str): creates a unique
        created_at: assigns current datetime
        updated_at: updates current datetime

    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Returns string representation of the object
        """

        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates the public instance attribute:
        'updated_at' - with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dict representation of the object
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
