#!/usr/bin/python3

"""The `amenity` module
This module defines one class, `Amenity(),
Amenity is sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place in the application.
    Attributes:
        name
    """

    name = ""
