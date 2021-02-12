#!/usr/bin/python3
""" This module contains a class State that inherits from BaseModel """

import json
import uuid
from datetime import datetime
from models import storage
from models import BaseModel


class State(BaseModel):
    """ State class
    """

    name = ""
