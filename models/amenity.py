#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity.
    Attributes:
        name (str): Name of the amenity.
    """

    name = ""
