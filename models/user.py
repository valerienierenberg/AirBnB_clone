#!/usr/bin/python3
""" This module contains a class User that inherits from BaseModel """

import json
import uuid
from datetime import datetime
from models import storage
from models import BaseModel


class User(BaseModel):
    """ User class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
