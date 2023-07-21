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

    def do_update(self, instance_name):
        """Updates an instance based on the class name and id
        Structure: update <class_name> <id> <name> <value>
        Arguments:
            <class_name>   The name of the class to update.
            <id>   The id of the class to update.
            <name>   The name of the class.
            <value>   The value of the class."""
        if not instance_name:
            print("** class name missing **")
            return

        tokens = shlex.split(instance_name)
        storage.reload()
        objs_dict = storage.all()
        if tokens[0] not in HBNBCommand.objs_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(tokens) == 1):
            print("** instance id missing **")
            return
        try:
            key = f"{tokens[0]}.{tokens[1]}"
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return

        if (len(tokens) == 2):
            print("** attribute name missing **")
            return
        if (len(tokens) == 3):
            print("** value missing **")
            return

        instance = objs_dict[key]
        if hasattr(instance, tokens[2]):
            data_type = type(getattr(instance, tokens[2]))
            setattr(instance, tokens[2], data_type(tokens[3]))
        else:
            setattr(instance, tokens[2], tokens[3])
        storage.save()

    def do_update2(self, instance_name):
        """Updates an instance based on the class name and id
        Structure: update <class_name> <id> <dictionary>
        Arguments:
            <class_name>   The name of the class to update.
            <id>   The id of the class to update.
            <dictionary>   The dictionary."""
        if not instance_name:
            print("** class name missing **")
            return

        dict_obj = "{" + instance_name.split("{")[1]
        tokens = shlex.split(instance_name)
        storage.reload()
        objs_dict = storage.all()
        if tokens[0] not in HBNBCommand.objs_dict.keys():
            print("** class doesn't exist **")
            return
        if (len(tokens) == 1):
            print("** instance id missing **")
            return
        try:
            key = f"{tokens[0]}.{tokens[1]}"
            objs_dict[key]
        except KeyError:
            print("** no instance found **")
            return

        if (dict_obj == "{"):
            print("** attribute name missing **")
            return

        dict_obj = dict_obj.replace("\'", "\"")
        dict_obj = json.loads(dict_obj)
        instance = objs_dict[key]
        for key in dict_obj:
            if hasattr(instance, key):
                data_type = type(getattr(instance, key))
                setattr(instance, key, dict_obj[key])
            else:
                setattr(instance, key, dict_obj[key])
        storage.save()

    def do_count(self, instance_name):
        """Retrieves the number of instances of a class"""
        count = 0
        for key in storage.all():
            if (instance_name in key):
                count += 1
        print(count)

    def default(self, instance_name):
        """Handles unusual ways of inputting data"""
        values_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        instance_name = instance_name.strip()
        values = instance_name.split(".")

        if len(values) != 2:
            cmd.Cmd.default(self, instance_name)
            return

        class_name = values[0]
        command = values[1].split("(")[0]
        line = ""

        if (command == "update" and values[1].split("(")[1][-2] == "}"):
            inputs = values[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = f"{class_name} {line}"
            self.do_update2(line.strip())
            return
        try:
            inputs = values[1].split("(")[1].split(",")
            for key in range(len(inputs)):
                if (key != len(inputs)-1):
                    line = line + " " + shlex.split(inputs[key])[0]
                else:
                    line = line + " " + shlex.split(inputs[key][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in values_dict.keys()):
            values_dict[command](line.strip())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
