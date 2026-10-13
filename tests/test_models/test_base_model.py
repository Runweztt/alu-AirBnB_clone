#!/usr/bin/python3
"""Unit tests for the BaseModel class."""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests the behavior of BaseModel."""

    def test_id_is_string(self):
        """Test that id is stored as a string."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_unique_ids(self):
        """Test that separate instances receive unique ids."""
        first = BaseModel()
        second = BaseModel()
        self.assertNotEqual(first.id, second.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime instance."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime instance."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that save changes the updated_at value."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, old_updated_at)

    def test_string_representation(self):
        """Test the required BaseModel string representation."""
        model = BaseModel()
        expected = "[BaseModel] ({}) {}".format(
            model.id, model.__dict__
        )
        self.assertEqual(str(model), expected)

    def test_to_dict_returns_dictionary(self):
        """Test that to_dict returns a dictionary."""
        model = BaseModel()
        self.assertIsInstance(model.to_dict(), dict)

    def test_to_dict_contains_class(self):
        """Test that dictionary contains the class name."""
        model = BaseModel()
        self.assertEqual(model.to_dict()["__class__"], "BaseModel")

    def test_to_dict_dates_are_strings(self):
        """Test that serialized dates are strings."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    def test_create_from_dictionary(self):
        """Test recreation of an instance from a dictionary."""
        model = BaseModel()
        model.name = "Test Model"
        model_dict = model.to_dict()

        new_model = BaseModel(**model_dict)

        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.name, new_model.name)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)
        self.assertIsNot(model, new_model)

    def test_class_not_added_from_kwargs(self):
        """Test that __class__ is ignored during reconstruction."""
        model = BaseModel()
        new_model = BaseModel(**model.to_dict())
        self.assertNotIn("__class__", new_model.__dict__)


if __name__ == "__main__":
    unittest.main()
