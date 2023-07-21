#!/usr/bin/python3
"""
User subclass that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class to represent new users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
