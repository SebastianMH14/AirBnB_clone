#!/usr/bin/python3
"""filestorage class"""

from models.base_model import BaseModel
import json
import os


class FileStorage:
    """create a class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""
        name = obj.__class__.__name__
        key = name + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to
        the JSON file (path: __file_path)"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(my_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        dic_t = {}
        with open(self.__file_path) as file:
            dic_t = json.load(file)
            for k, v in dic_t.items():
                obj = v["__class__"]
                self.__objects[k] = locals()[obj](**v)
