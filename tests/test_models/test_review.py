#!/usr/bin/python3

import unittest
from models.review import Review
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.storage = FileStorage()
        self.review.place_id = "place id"
        self.review.user_id = "user id"
        self.review.text = "some text"

    def tearDown(self):
        self.storage._FileStorage__object = {}

    def test_attributes(self):
        self.assertEqual(self.review.place_id, "place id")
        self.assertEqual(self.review.user_id, "user id")
        self.assertEqual(self.review.text, "some text")
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)
        self.assertIsNotNone(self.review.id)


if __name__ == "__main__":
    unittest.main()
