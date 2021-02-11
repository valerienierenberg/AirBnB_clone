#!/usr/bin/python3
""" This module contains a class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances
"""


import json

class FileStorage:
    """ class FileStorage """

    __objects = {}
    __file_path = "file.json"

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects["key"] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w") as file:
            json.dump(__objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if self.__file_path is None:
            return
        else:
            with open(self.__file_path, "r") as file:
                json.loads(file.read())
