#!/usr/bin/python3
"""Unit tests for the Review class."""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review model."""

    def test_review(self):
        """Test Review inheritance and default attributes."""
        review = Review()

        self.assertIsInstance(review, BaseModel)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
