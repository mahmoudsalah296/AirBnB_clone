#!/usr/bin/python3
"""Amenity Module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        super().__init__(*args, **kwargs)
