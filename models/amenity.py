#!/usr/bin/python3
""" This module contains a class Amenity that inherits from BaseModel """

import json
import uuid
from datetime import datetime
from models import storage
from models import BaseModel


class Amenity(BaseModel):
    """ Amenity class
    """

    name = ""
