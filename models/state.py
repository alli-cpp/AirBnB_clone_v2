#!/usr/bin/python3

"""The `state` module
This module defines one class, `State(),
State() sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.
    Attributes:
        name
    """
    name = ""
