#!/usr/bin/python3
"""Defines the Review model."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review for a place."""

    place_id = ""
    user_id = ""
    text = ""
