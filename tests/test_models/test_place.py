#!/usr/bin/python3

import unittest
from models.place import Place
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.storage = FileStorage()
        self.place.city_id = "city id"
        self.place.user_id = "user id"
        self.place.name = "Isaac"
        self.place.description = "description"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 5
        self.place.price_by_night = 5000
        self.place.latitude = 30.6
        self.place.longitude = 30.6
        self.place.amenity_ids = ["id 1", "id 2"]

    def tearDown(self):
        self.storage._FileStorage__object = {}

    def test_attributes(self):
        self.assertEqual(self.place.city_id, "city id")
        self.assertEqual(self.place.user_id, "user id")
        self.assertEqual(self.place.name, "Isaac")
        self.assertEqual(self.place.description, "description")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 5)
        self.assertEqual(self.place.price_by_night, 5000)
        self.assertEqual(self.place.latitude, 30.6)
        self.assertEqual(self.place.longitude, 30.6)
        self.assertEqual(self.place.amenity_ids, ["id 1", "id 2"])
        self.assertIsNotNone(self.place.created_at)
        self.assertIsNotNone(self.place.updated_at)
        self.assertIsNotNone(self.place.id)


if __name__ == "__main__":
    unittest.main()
