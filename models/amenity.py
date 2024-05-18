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
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class with optional arguments
        provided in kwargs.

        Parameters:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        self.name = ""
