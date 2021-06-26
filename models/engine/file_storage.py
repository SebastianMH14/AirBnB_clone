#!/usr/bin/python3
"""filestorage class"""


class FileStorage:
    """create a class"""
    __file_path = ...
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
