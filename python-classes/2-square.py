#!/usr/bin/python3
"""Module that defines a Square class with validated size attribute."""


class Square:
    """Class that defines a square."""
    size = 0
    def __init__(self, size):
        """Initialize a new Square with a given size, after validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
