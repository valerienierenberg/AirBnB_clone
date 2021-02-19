#!/usr/bin/python3
""" This module contains a class BaseModel that defines
all common attributes/methods for other classes """

from datetime import datetime
import json
import models
import uuid


class BaseModel:
    """Base Class
    """

    def __init__(self, *args, **kwargs):
        """__init method
        """
        if len(kwargs) != 0:  # as long as it's not empty
            for key, value in kwargs.items():  # iterating through dictionary
                if key == "created_at" or key == "updated_at":  # cnvrt to dt
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)  # sets attribute
                elif key != "__class__":  # class should not be added as attr
                    setattr(self, key, value)  # setting attr for other keys
        else:  # if kwargs is empty
            self.id = str(uuid.uuid4())  # create id and created_at
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ __str method:
        Args: self
        Return: [<class name>] (<self.id>) <self.__dict__>
        """
        return ("[{}] ({}) {}".format(str(type(self).__name__),
                                      self.id, self.__dict__))
# ^ printing id and dictionary in str format

    def save(self):
        """ save method:
            updates public instance attribute 'updated_at' w/ current datetime
        Args: self
        """
        self.updated_at = datetime.now()  # updates time to be current time
        models.storage.save()

    def to_dict(self):
        """ to_dict method:
            returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        my_dict = dict(self.__dict__)  # make variable my_dict
        my_dict["__class__"] = str(type(self).__name__)
# ^ adds class key with class name of the object
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
# ^ convert keys to string objects at iso format
        return my_dict
