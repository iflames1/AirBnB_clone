#!/usr/bin/python3

import unittest
from models.city import City
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.storage = FileStorage()
        self.city.state_id = "state id"
        self.city.name = "Isaac"

    def tearDown(self):
        self.storage._FileStorage__object ={}

    def test_attributes(self):
        self.assertEqual(self.city.name, "Isaac")
        self.assertEqual(self.city.state_id, "state id")
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)
        self.assertIsNotNone(self.city.id)

if __name__ == "__main__":
    unittest.main()
