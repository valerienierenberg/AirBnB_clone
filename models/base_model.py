#!/usr/bin/python3
""" This module contains a class BaseModel that defines
all common attributes/methods for other classes """

import json
import uuid
from datetime import datetime

class BaseModel:
    """Base Class
    """

    def __init__(self):
        """__init method
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()  # probably need to add something here. or somewhere else? in a method?

    def __str__(self):
        """ __str method:
        Args: self
        Return: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(type(self.__name__), self.id, self.__dict__))

