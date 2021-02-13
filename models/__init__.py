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