#!/usr/bin/python3
"""
This module provides a function for adding two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers
    
    Args:
        a: First integer or float
        b: Second integer or float (default: 98)
    
    Returns:
        The sum of a and b as an integer
    
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
