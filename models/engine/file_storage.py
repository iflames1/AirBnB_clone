#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    CLASSES = {"BaseModel": BaseModel}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        with open(self.__file_path, 'r') as file:
            loaded_objects = json.load(file)
            for key, value in loaded_objects.items():
                class_name = value["__class__"]
                if class_name in self.CLASSES:
                    instance = self.CLASSES[class_name](**value)
                    self.__objects[key] = instance

    #def reload(self):
    #    try:
    #        with open(self.__file_path, 'r') as file:
    #            loaded_objects = json.load(file)
    #            for key, obj_dict in loaded_objects.items():
    #                class_name, obj_id = key.split('.')
    #                # Implement logic to recreate instances from obj_dict
    #                # Example: new_instance = BaseModel(**obj_dict)
    #                self.__objects[key] = new_instance
    #    except FileNotFoundError:
    #        pass
