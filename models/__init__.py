#!/usr/bin/python3
""" init file """

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine import file_storage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"BaseModel": BaseModel, "City": City, "Place": Place, "Amenity":
           Amenity, "Review": Review, "State": State, "User": User}

storage = file_storage.FileStorage()
storage.reload()
