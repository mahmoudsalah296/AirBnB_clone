#!/usr/bin/python3
"""This is a module for BaseModel class for AirBnB"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel doc string"""

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

            # Add the object to the storage
            models.storage.new(self)

    def __str__(self):
        """str method of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update update_at attribute with current datetime"""
        self.updated_at = datetime.now()

        # Save the objects to the JSON file
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/value of the instance"""
        date_dict = self.__dict__.copy()
        date_dict["__class__"] = self.__class__.__name__
        date_dict["created_at"] = self.created_at.isoformat()
        date_dict["updated_at"] = self.updated_at.isoformat()
        return date_dict
