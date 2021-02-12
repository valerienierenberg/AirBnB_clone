#!/usr/bin/python3
""" This module contains a class Review that inherits from BaseModel """

import json
import uuid
from datetime import datetime
from models import storage
from models import BaseModel


class Review(BaseModel):
    """ Review class
    """

    place_id = ""  # it will be the Place.id
    user_id = ""  # it will be the User.id
    text = ""
