#!/usr/bin/python3

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()
        self.storage = FileStorage()
        self.amenity.name = "Isaac"

    def tearDown(self):
        self.storage._FileStorage__object = {}

    def test_attributes(self):
        self.assertEqual(self.amenity.name, "Isaac")
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)
        self.assertIsNotNone(self.amenity.id)


if __name__ == "__main__":
    unittest.main()
