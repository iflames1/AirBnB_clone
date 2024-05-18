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
    name = ""
