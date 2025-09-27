#!/usr/bin/python3
"""Module that provides a function to check if an object is an instance of a class that inherited from a specified class."""

"""Module that provides a function to check if an object is an instance 
of a class that inherited from a specified class."""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    
    Args:
        obj: The object to check
        a_class: The class to check inheritance against
    
    Returns:
        bool: True if obj's class is a subclass of a_class, False otherwise
    """

    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class != a_class
