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
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """ __str method:
        Args: self
        Return: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """ save method:
            updates public instance attribute 'updated_at' w/ current datetime
        Args: self
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ to_dict method:
            returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        my_dict = dict(self.__dict__)
        my_dict["__class__"] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()

        return my_dict
