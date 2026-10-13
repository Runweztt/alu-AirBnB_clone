#!/usr/bin/python3
"""Unit tests for the Amenity class."""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the Amenity model."""

    def test_amenity(self):
        """Test Amenity inheritance and default name."""
        amenity = Amenity()

        self.assertIsInstance(amenity, BaseModel)
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
