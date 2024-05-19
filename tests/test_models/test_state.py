#!/usr/bin/python3

import unittest
from models.state import State
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.storage = FileStorage()
        self.state.name = "Flames"

    def tearDown(self):
        self.storage._FileStorage__object = {}

    def test_attributes(self):
        self.assertEqual(self.state.name, "Flames")
        self.assertIsNotNone(self.state.created_at)
        self.assertIsNotNone(self.state.updated_at)
        self.assertIsNotNone(self.state.id)


if __name__ == "__main__":
    unittest.main()
