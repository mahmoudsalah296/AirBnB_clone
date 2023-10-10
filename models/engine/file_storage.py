#!/usr/bin/python3
""""""
import json
import os
import sys

from models.base_model import BaseModel


class FileStorage:
    """"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        # key = <obj class name>.id
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value

        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file, indent=2)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)

                for key, value in obj_dict.items():
                    class_name, class_id = key.split(".")

                    # Dynamically create an instance of the corresponding class
                    class_instance = getattr(sys.modules[__name__], class_name, None)
                    if class_instance:
                        obj = class_instance(**value)
                        FileStorage.__objects[key] = obj
