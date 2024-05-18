#!/usr/bin/python3

"""
Base class for all models in the application. Provides common functionality
for managing model instances, such as generating unique IDs, tracking
creation and update timestamps, and serializing/deserializing model data.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all models in the application. Provides common functionality
    for managing model instances, such as generating unique IDs, tracking
    creation and update timestamps, and serializing/deserializing model data.

    Attributes:
        id (str): Unique identifier for the model instance.
        created_at (datetime): Timestamp of when the model instance was
        created.
        updated_at (datetime): Timestamp of when the model instance was last
        updated.

    Methods:
        __init__(self, *args, **kwargs): Initializes a new model instance,
        either from a dictionary of attributes or by generating a new ID and
        timestamps.
        __str__(self) -> str: Returns a string representation of the model
        instance.
        save(self): Saves the current state of the model instance to
        persistent storage and updates the `updated_at` timestamp.
        to_dict(self): Returns a dictionary representation of the model
        instance, including the `__class__` attribute.
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
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if not kwargs or "__class__" not in kwargs:
            models.storage.new(self)

    def __str__(self) -> str:
        """
        A description of the entire function, its parameters, and its return
        types.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save the object to the database and update the 'updated_at' attribute.
        No parameters.
        No return value.
        """
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        A method to convert the object instance into a dictionary
        representation.
        Returns:
            dict: A dictionary containing the object's attributes along with
            '__class__', 'created_at', and 'updated_at' keys.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
