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

classes = {"BaseModel": BaseModel, "City": City, "Place": Place, "Amenity": Amenity,
            "Review": Review, "State": State, "User": User}

storage = file_storage.FileStorage()
storage.reload()
<<<<<<< HEAD

"""
base_model.py
user.py
state.py
city.py
amenity.py
place.py
review.py
engine/
    file_storage.py
    __init__.py
"""

console.py
models
    __init__.py
    amenity.py
    base_model.py
    city.py
    place.py
    review.py
    state.py
    user.py
    engine
        __init__.py
        file_storage.py
=======
>>>>>>> 4419a3545a78abca15d9eae785803e799aa6cd21
