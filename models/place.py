#!/usr/bin/python3
"""
Represents a place, which is a type of BaseModel. A place has various
attributes
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place, which is a type of BaseModel. A place has various
    attributes such as city ID, user ID, name, description, number of rooms,
    number of bathrooms, maximum number of guests, price per night, latitude,
    longitude, and a list of amenity IDs.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can
        accommodate.
        price_by_night (int): The price per night to stay at the place.
        latitude (float): The latitude coordinate of the place's location.
        longitude (float): The longitude coordinate of the place's location.
        amenity_ids (list): A list of IDs for the amenities available at the
        place.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Place class.

        Parameters:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
