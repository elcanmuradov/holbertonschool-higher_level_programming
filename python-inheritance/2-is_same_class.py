#!/usr/bin/python3
"""Module that check the object"""
def is_same_class(obj, a_class):
    """Returns true or false"""

    if type(obj) is a_class:
        return True
    else:
        return False