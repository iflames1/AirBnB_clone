#!/usr/bin/python3

import unittest
import json
from models.review import Review
from models.engine.file_storage import FileStorage

class TestUser(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.storage = FileStorage()
        self.review.place_id = "place id"


    def tearDown(self):
        self.storage._FileStorage__object ={}

    def test_attributes(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "Isaac")
        self.assertEqual(self.user.last_name, "Flames")
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)
        self.assertIsNotNone(self.user.id)

if __name__ == "__main__":
    unittest.main()