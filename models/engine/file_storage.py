#!/usr/bin/python3
"""Defines the file storage engine for AirBnB objects."""

import json


class FileStorage:
    """Serialize objects to JSON and deserialize them from JSON."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary containing all stored objects."""
        return self.__objects

    def new(self, obj):
        """Add an object to the storage dictionary."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize all stored objects to the JSON file."""
        objects = {
            key: obj.to_dict() for key, obj in self.__objects.items()
        }
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(objects, file)

    def reload(self):
        """Deserialize objects from the JSON file when it exists."""
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User,
        }

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                objects = json.load(file)
        except FileNotFoundError:
            return

        for key, value in objects.items():
            class_name = value.get("__class__")
            model_class = classes.get(class_name)

            if model_class is not None:
                self.__objects[key] = model_class(**value)
