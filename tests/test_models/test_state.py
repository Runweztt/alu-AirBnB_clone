#!/usr/bin/python3
"""Unit tests for the State class."""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test the State model."""

    def test_state(self):
        """Test State inheritance and default name."""
        state = State()

        self.assertIsInstance(state, BaseModel)
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
