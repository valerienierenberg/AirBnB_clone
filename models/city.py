#!/usr/bin/python3
""" This module contains a class City that inherits from BaseModel """

from datetime import datetime
import json
from models.engine import file_storage
from models.base_model import BaseModel
import uuid


class City(BaseModel):
    """ City class
    """

    state_id = ""  # will be State.id
    name = ""
