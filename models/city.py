#!/usr/bin/python3
"""Defines the City model."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city."""

    state_id = ""
    name = ""
