#!/usr/bin/python3
"""
Review subclass that inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that represents new reviews"""
    place_id = ""
    user_id = ""
    text = ""
