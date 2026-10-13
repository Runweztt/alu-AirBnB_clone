#!/usr/bin/python3
"""Unit tests for the BaseModel class."""

import os
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test the behavior of BaseModel."""

    def tearDown(self):
        """Reset storage after each test."""
        storage.all().clear()

        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_id_is_string(self):
        """Test that id is a string."""
        self.assertIsInstance(BaseModel().id, str)

    def test_ids_are_unique(self):
        """Test that instances receive unique ids."""
        self.assertNotEqual(BaseModel().id, BaseModel().id)

    def test_dates_are_datetime_objects(self):
        """Test that dates are datetime objects."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that save updates updated_at."""
        model = BaseModel()
        old_time = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, old_time)

    def test_string_representation(self):
        """Test the required string representation."""
        model = BaseModel()

        expected = "[BaseModel] ({}) {}".format(
            model.id,
            model.__dict__
        )

        self.assertEqual(str(model), expected)

    def test_to_dict(self):
        """Test dictionary serialization."""
        model = BaseModel()
        data = model.to_dict()

        self.assertEqual(data["__class__"], "BaseModel")
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)

    def test_create_from_dictionary(self):
        """Test recreation from a dictionary."""
        model = BaseModel()
        model.name = "Test Model"

        copy = BaseModel(**model.to_dict())

        self.assertEqual(model.id, copy.id)
        self.assertEqual(copy.name, "Test Model")
        self.assertIsInstance(copy.created_at, datetime)
        self.assertIsNot(model, copy)
        self.assertNotIn("__class__", copy.__dict__)


if __name__ == "__main__":
    unittest.main()
