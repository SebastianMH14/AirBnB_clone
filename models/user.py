#!/usr/bin/python3
"""Creating a user class"""
"""empty strings"""

from models import base_model
from models.base_model import BaseModel

class User(BaseModel):
    """class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
