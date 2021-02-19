#!/usr/bin/python3
""" This module contains a class State that inherits from BaseModel """

from datetime import datetime
import json
from models.engine import file_storage
from models.base_model import BaseModel
import uuid


class State(BaseModel):
    """ State class
    """

    name = ""
