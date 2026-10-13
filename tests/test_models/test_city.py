#!/usr/bin/python3
"""Unit tests for the City class."""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City model."""

    def test_city(self):
        """Test City inheritance and default attributes."""
        city = City()

        self.assertIsInstance(city, BaseModel)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
