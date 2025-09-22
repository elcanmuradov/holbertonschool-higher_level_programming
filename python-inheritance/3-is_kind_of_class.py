#!/usr/bin/python3
"""
Module that contains is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class; otherwise
    Args:
        obj: The object to check
        a_class: The class to check against
    Returns:
        bool: True if obj is an instance of a_class or inherits from it, False 
    """
    return isinstance(obj, a_class)