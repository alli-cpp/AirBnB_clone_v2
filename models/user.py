#!usr/bin/python3

"""The `user` module
This module defines one class, `user(),
user() sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User creates a new user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            super().__init__()

        # if kwargs have values
        if len(kwargs) > 0:
            super().__init__(**kwargs)
