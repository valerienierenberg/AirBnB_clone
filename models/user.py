#!/usr/bin/python3
""" This module contains a class User that inherits from BaseModel """

from datetime import datetime
import json
from models.engine import file_storage
from models.base_model import BaseModel
import uuid


class User(BaseModel):
    """ User class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
