#!/usr/bin/python3
""" This module contains a class FileStorage that serializes
instances to a JSON file and deserializes JSON file to instances
"""


import json
from os.path import exists


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
        empty_dict = {}
        for key, value in self.__objects.items():
            empty_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(empty_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                content = json.load(file)
                print(content)

# we need to figure out how to store ^content into __objects by <class name>.id
#        self.__objects = {}  # "__objects will store by <class name>.id"
#        for key, value in content.items():
#            self.__objects[key] = content[value]
