#!/usr/bin/python3

"""The `amenity` module
This module defines one class, `Amenity(),
Amenity is sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
