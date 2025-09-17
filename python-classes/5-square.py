#!/usr/bin/python3
"""Module that defines a Square class with size validation and area."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size."""
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size ** 2
    def my_print(self):
        """Print console the square"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for k in range(0, self.__size):
                print("#", end="")
            print()
