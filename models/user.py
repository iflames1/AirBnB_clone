#!/usr/bin/python3
"""
Represents a user in the application.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user in the application.

    The `User` class inherits from the `BaseModel` class and provides
    properties for storing a user's email, password, first name, and last name.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
