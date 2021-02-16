#!/usr/bin/python3
""" init file """

from models.engine import file_storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review

classes = {"BaseModel": BaseModel, "City": City, "Place": Place, "Amenity":
           Amenity, "Review": Review, "State": State, "User": User}

storage = file_storage.FileStorage()
storage.reload()
