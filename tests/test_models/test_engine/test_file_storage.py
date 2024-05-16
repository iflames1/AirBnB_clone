#!/usr/bin/python3


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json

class TestFileStorage(unittest.TestCase):

    def setUp(self) -> None:
        self.storage = FileStorage()
        self.file_path = FileStorage.get_file_path(self) #self.storage._FileStorage__file_path # replace with getter

    def tearDown(self) -> None:
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        all_object = self.storage.all()
        self.assertEqual(len(all_object), 2)
        self.assertIn(obj1.__class__.name__ + '.' + obj1.id, all_object)
        self.assertIn(obj1.__class__.name__ + '.' + obj2.id, all_object)

    def test_new_method(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, self.storage.all())

    def test_save_method(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
            self.assertIn(obj.__class__.__name__ + '.' + obj.id, saved_data)

    def test_reload_method(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(obj.__class__.__name__ + '.' + obj.id, self.storage.all())

if __name__ == "__main__":
    unittest.main()
