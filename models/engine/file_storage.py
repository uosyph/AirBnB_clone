#!/usr/bin/python3
"""
Engine class that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
from os import path


class FileStorage():
    """Serialize instances to JSON file
    and deserialize JSON files to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new object"""
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes object to the JSON file"""
        obj = {}
        for key in FileStorage.__objects:
            obj[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj, f)

    def reload(self):
        """Deserializes the JSON file to object"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        dict_obj = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        if not path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path) as f:
            objs = json.load(f)
            FileStorage.__objects = {}
            for key in objs:
                FileStorage.__objects[key] = \
                    dict_obj[key.split(".")[0]](**objs[key])
