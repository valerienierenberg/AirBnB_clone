#!/usr/bin/python3
""" This module contains a class City that inherits from BaseModel """

import json
import uuid
from datetime import datetime
from models import storage
from models import BaseModel


class City(BaseModel):
    """ City class
    """

    state_id = ""  # will be State.id
    name = ""
