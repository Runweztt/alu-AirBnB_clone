#!/usr/bin/python3
"""Defines the User model."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent an AirBnB user."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
