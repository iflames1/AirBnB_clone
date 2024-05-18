#!/usr/bin/python3
"""
Initializes a new instance of the class with optional arguments provided in
kwargs.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity in the application.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
