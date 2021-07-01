#!/usr/bin/python3
"""Creating a user class"""

from models import base_model
from models.base_model import BaseModel


class User(BaseModel):
    """class user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
