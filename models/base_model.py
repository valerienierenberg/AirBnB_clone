#!/usr/bin/python3
""" This module contains a class BaseModel that defines
all common attributes/methods for other classes """

import json
import uuid
from datetime import datetime


class BaseModel:
    """Base Class
    """

    def __init__(self, *args, **kwargs):
        """__init method
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                elif key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
        else:
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
