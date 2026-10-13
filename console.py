#!/usr/bin/python3
"""Defines the command interpreter for the AirBnB clone."""

import cmd
import shlex
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Provide commands to create and manage AirBnB objects."""

    prompt = "(hbnb) "

    classes = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User,
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF is received."""
        print()
        return True

    def _parse(self, arg):
        """Split command arguments while preserving quoted strings."""
        return shlex.split(arg)

    def _validate_class(self, args):
        """Validate that a command includes a supported class name."""
        if not args:
            print("** class name missing **")
            return None

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return None

        return args[0]

    def _get_object(self, class_name, object_id):
        """Return an object using its class name and id."""
        key = "{}.{}".format(class_name, object_id)
        return storage.all().get(key)

    def do_create(self, arg):
        """Create a new instance, save it, and print its id."""
        args = self._parse(arg)
        class_name = self._validate_class(args)

        if class_name is None:
            return

        obj = self.classes[class_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print the string representation of a stored instance."""
        args = self._parse(arg)
        class_name = self._validate_class(args)

        if class_name is None:
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj = self._get_object(class_name, args[1])

        if obj is None:
            print("** no instance found **")
            return

        print(obj)

    def do_destroy(self, arg):
        """Delete an instance and save the storage change."""
        args = self._parse(arg)
        class_name = self._validate_class(args)

        if class_name is None:
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all instances, optionally filtered by class."""
        args = self._parse(arg)

        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        objects = []

        for obj in storage.all().values():
            if not args or obj.__class__.__name__ == args[0]:
                objects.append(str(obj))

        print(objects)

    def _cast_value(self, obj, attr_name, value):
        """Cast an updated attribute value to its existing type."""
        if not hasattr(obj, attr_name):
            return value

        current = getattr(obj, attr_name)

        if isinstance(current, bool):
            return value.lower() in ("true", "1", "yes")

        if isinstance(current, int):
            return int(value)

        if isinstance(current, float):
            return float(value)

        return value

    def do_update(self, arg):
        """Update one attribute of a stored instance."""
        args = self._parse(arg)
        class_name = self._validate_class(args)

        if class_name is None:
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj = self._get_object(class_name, args[1])

        if obj is None:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        value = self._cast_value(obj, attr_name, args[3])

        setattr(obj, attr_name, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
