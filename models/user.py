#!/usr/bin/python3
"""
File containing User class for AirBnB - The Console
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
