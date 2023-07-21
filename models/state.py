#!/usr/bin/python3
"""
State subclass that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class to represents new states"""
    name = ""
