#!/usr/bin/python3
"""
Represents a review for a place.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review for a place.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who left the review.
        text (str): The text of the review.
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
        self.place_id = ""
        self.user_id = ""
        self.text = ""
