#!/usr/bin/python3
""""""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()
        self.base_model.name = "My First Model"
        self.base_model.my_number = 89

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)

    def test_id_type(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_id_unique(self):
        self.unique_id = BaseModel()
        self.assertNotEqual(self.unique_id.id, self.base_model.id)

    def test_created_at_and_updated_at(self):
        now = datetime.now()
        self.assertLessEqual(self.base_model.created_at, now)
        self.assertLessEqual(self.base_model.updated_at, now)

    def test_save_method(self):
        previous_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(previous_updated_at, self.base_model.updated_at)
        self.assertLessEqual(self.base_model.created_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsNotNone(obj_dict["id"])
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], self.base_model.id)
        self.assertEqual(obj_dict["created_at"], self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], self.base_model.updated_at.isoformat())
        self.assertEqual(obj_dict["name"], self.base_model.name)
        self.assertEqual(obj_dict["my_number"], self.base_model.my_number)
        """ for key in obj_dict:
            self.assertEqual(obj_dict[key], self.base_model.key) """

    def test_str_method(self):
        obj_str = str(self.base_model)
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(obj_str, expected_str)


if __name__ == "__main__":
    unittest.main()
