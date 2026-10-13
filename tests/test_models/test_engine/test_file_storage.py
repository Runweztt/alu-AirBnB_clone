#!/usr/bin/python3
"""Unit tests for the FileStorage class."""

import json
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test JSON serialization and deserialization."""

    def setUp(self):
        """Prepare isolated storage for each test."""
        self.storage = FileStorage()
        self.storage.all().clear()
        self.storage._FileStorage__file_path = "test_file.json"

    def tearDown(self):
        """Remove temporary test data."""
        self.storage.all().clear()

        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def test_all_returns_dictionary(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new adds an object."""
        model = BaseModel()
        self.storage.new(model)

        key = "BaseModel.{}".format(model.id)

        self.assertIn(key, self.storage.all())

    def test_save_writes_json(self):
        """Test that save writes JSON data."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()

        self.assertTrue(os.path.exists("test_file.json"))

        with open("test_file.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        self.assertIn("BaseModel.{}".format(model.id), data)

    def test_reload_recreates_object(self):
        """Test that reload recreates serialized objects."""
        model = BaseModel()
        key = "BaseModel.{}".format(model.id)

        with open("test_file.json", "w", encoding="utf-8") as file:
            json.dump({key: model.to_dict()}, file)

        self.storage.all().clear()
        self.storage.reload()

        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)


if __name__ == "__main__":
    unittest.main()
