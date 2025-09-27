#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.
    """
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class != a_class
