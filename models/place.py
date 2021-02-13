#!/usr/bin/python3
""" This module contains a class Place that inherits from BaseModel """

import json
import uuid
from datetime import datetime
from models.engine import file_storage
from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class
    """

    city_id = ""  # it will be the City.id
    user_id = ""  # it will be the User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # it will be the list of Amenity.id later
