#!/usr/bin/python3
"""
Class subclass that inherits from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class to represent new cities"""
    state_id = ""
    name = ""
