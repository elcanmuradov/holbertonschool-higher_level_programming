#!/usr/bin/python3
"""Module that defines a Square class with validated area attribute."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):

        """Find area of initizialied Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Find area of initizialied Square"""
    def area(self):
        return self.size * self.size
