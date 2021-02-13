#!/usr/bin/python3
""" This module contains a class State that inherits from BaseModel """

import json
import uuid
from datetime import datetime
from models.engine import file_storage
from models.base_model import BaseModel


class State(BaseModel):
    """ State class
    """

    name = ""
