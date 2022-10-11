#!/usr/bin/python3

"""The `amenity` module
This module defines one class, `Amenity(),
Amenity is sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Public class attributes:
        name: string - empty string
    """
    name = ''

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
