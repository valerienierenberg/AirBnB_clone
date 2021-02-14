#!/usr/bin/python3
""" init file """

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

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
