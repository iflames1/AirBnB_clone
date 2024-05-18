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

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
