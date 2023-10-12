#!/usr/bin/python3
"""a module for user class that inherit from base class"""

from models.base_model import BaseModel


class User(BaseModel):
    """a class for users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
