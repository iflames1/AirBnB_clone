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

    place_id = ""
    user_id = ""
    text = ""
