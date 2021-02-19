#!/usr/bin/python3
""" This module contains a class Review that inherits from BaseModel """

from datetime import datetime
import json
from models.engine import file_storage
from models.base_model import BaseModel
import uuid


class Review(BaseModel):
    """ Review class
    """

    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
