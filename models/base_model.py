#!/usr/bin/python3
"""Defines the BaseModel class for all AirBnB objects."""

from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Defines common attributes and methods for other models."""

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                if key in ("created_at", "updated_at"):
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """Update updated_at and save the object to file storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
