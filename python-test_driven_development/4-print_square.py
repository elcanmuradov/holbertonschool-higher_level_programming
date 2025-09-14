#!/usr/bin/python3
"""
This module contains a function to print a square with the character '#'.
It handles type validation and size validation.
The function prints a square of specified size using '#' characters.
"""


def print_square(size):
    """
    Prints a square with the character '#'.
    Size determines the length and width of the square.
    """
    # Check if size is a float (regardless of value)
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Print the square
    for i in range(size):
        print("#" * size)