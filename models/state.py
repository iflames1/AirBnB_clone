#!/usr/bin/python3
"""
Represents a state in the application.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state in the application.

    Attributes:
        name (str): The name of the state.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class with optional arguments
        provided in kwargs.

        Parameters:
            *args (tuple): Variable length argument list.
            **kwargs (dict): Arbitrary keyword arguments.

        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        self.name = ""
