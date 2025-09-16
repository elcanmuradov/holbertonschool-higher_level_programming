#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""

class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a new Square with a given size (no validation)."""
        self.__size = size
