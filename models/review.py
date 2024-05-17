#!/usr/bin/python3

from models.base_model import BaseModel
from models.place import Place
from models.user import User

class Review(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = Place.id
        self.user_id = User.id
        self.text = ""
