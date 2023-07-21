#!/usr/bin/python3
"""
The entry point of the command interpreter
"""

import cmd
import json
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The command interpreter"""

    prompt = "(hbnb) "
    objs_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def emptyline(self):
        """Overrides the emptyline method """
        pass

    def do_nothing(self, arg):
        """Does nothing"""
        pass

    def do_quit(self, arg):
        """Saves the data before closing the application"""
        return True

    def do_EOF(self, arg):
        """Saves the data before closing the application using CTRL+D"""
        print("")
        return True

    def do_create(self, instance_name):
        """Creates a new instance
        Structure: create <class_name>
        Arguments:
            <class_name>   The name of the class to create."""
        if not instance_name:
            print("** class name missing **")
            return

        tokens = shlex.split(instance_name)
        if tokens[0] not in HBNBCommand.objs_dict.keys():
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.objs_dict[tokens[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, instance_name):
        """Prints the string representation of an instance
        Structure: show <class_name> <id>
        Arguments:
            <class_name>   The name of the class to show.
            <id>   The id of the class to show."""
        tokens = shlex.split(instance_name)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.objs_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return

        storage.reload()
        objs_dict = storage.all()

        key = f"{tokens[0]}.{tokens[1]}"
        if key in objs_dict:
            print(str(objs_dict[key]))
        else:
            print("** no instance found **")

    def do_destroy(self, instance_name):
        """Deletes an instance based on the class name
        Structure: destroy <class_name> <id>
        Arguments:
            <class_name>   The name of the class to delete.
            <id>   The id of the class to delete."""
        tokens = shlex.split(instance_name)
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.objs_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return

        storage.reload()
        objs_dict = storage.all()

        key = f"{tokens[0]}.{tokens[1]}"
        if key in objs_dict:
            del objs_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, instance_name):
        """Prints string represention of all instances of a given class
        Structure: all <class_name> <'all'>
        Arguments:
            <class_name>   The name of the class to show.
            'all'   Shows all classes."""
        storage.reload()
        json_obj = []
        objs_dict = storage.all()

        if not instance_name:
            for key in objs_dict:
                json_obj.append(str(objs_dict[key]))
            print(json.dumps(json_obj))
            return

        token = shlex.split(instance_name)
        if token[0] in HBNBCommand.objs_dict.keys():
            for key in objs_dict:
                if token[0] in key:
                    json_obj.append(str(objs_dict[key]))
            print(json.dumps(json_obj))
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
