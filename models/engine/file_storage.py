#!/usr/bin/python3
"""
The `FileStorage` class is responsible for managing the persistence of objects
in a JSON file. It provides methods to create, retrieve, update, and delete
objects, as well as to save and reload the object state from the file.

The `CLASSES` attribute is a dictionary that maps class names to their
corresponding model classes, allowing the `FileStorage` class to instantiate
the appropriate class when loading objects from the JSON file.

The `__file_path` attribute stores the path to the JSON file where the object
data is stored.

The `__objects` attribute is a dictionary that stores the instantiated
objects, with the object's key (class name and ID) as the dictionary key.

The `all()` method returns the dictionary of all instantiated objects.

The `new(obj)` method adds a new object to the `__objects` dictionary, using
the object's class name and ID as the key.

The `save()` method serializes all the objects in the `__objects` dictionary to
a JSON file specified by the `__file_path` attribute.

The `reload()` method loads the object data from the JSON file specified by the
`__file_path` attribute and instantiates the appropriate objects based on the
class names stored in the file.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage classj
    """
    CLASSES = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Review": Review}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all instantiated objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the '__objects' dictionary with the key formatted
        as '{obj.__class__.__name__}.{obj.id}'.

        Parameters:
            obj: The object to be added to the dictionary.

        Returns:
            None
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Saves the current state of the model instance to persistent storage
        and updates the `updated_at` timestamp.
        """
        serialized_objects = {key: obj.to_dict()
                              for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Attempts to reload the object data from a JSON file specified by the
        `__file_path` attribute.
        Iterates through the loaded objects, instantiates the corresponding
        class instances, and stores them in `__objects` dictionary.
        """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name = value["__class__"]
                    if class_name in self.CLASSES:
                        instance = self.CLASSES[class_name](**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
