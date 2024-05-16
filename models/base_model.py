#!/usr/bin/python3
"""
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        if not kwargs or "__class__" not in kwargs:
            models.storage.new(self)

    def __str__(self) -> str:
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
