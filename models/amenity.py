#!/usr/bin/python3
"""
Amenity subclass that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that represents new amenities"""
    name = ""
