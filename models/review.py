#!/usr/bin/python3
"""Creating a class Review"""


from models.base_model import BaseModel


class Review(BaseModel):
    """class review"""
    place_id = ""
    user_id = ""
    text = ""
