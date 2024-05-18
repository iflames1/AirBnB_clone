#!/usr/bin/python3
"""
Represents a city.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
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
        self.state_id = ""
        self.name = ""
