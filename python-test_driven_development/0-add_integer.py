#!/usr/bin/python3
"""
This module contains a function to add two integers.
It handles type validation and conversion from floats.
The function provides default values and error handling.
"""


def add_integer(a, b=98):
    """
    Adds two integers together.
    Converts floats to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)