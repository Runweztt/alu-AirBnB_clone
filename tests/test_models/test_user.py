#!/usr/bin/python3
"""Unit tests for the User class."""

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User model."""

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(User(), BaseModel)

    def test_default_attributes(self):
        """Test default User attributes."""
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
