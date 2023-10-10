#!/usr/bin/python3
"""This is a module for BaseModel class for AirBnB"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """initialization method"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("updated_at", "created_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """str method of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update update_at attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/value of the instance"""
        attrs = {}
        attrs["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if type(value) == datetime:
                # convert datetime to iso format and to a string
                attrs[key] = str(value.isoformat())
            else:
                attrs[key] = value
        return attrs
