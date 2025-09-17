#!/usr/bin/python3
"""Module that defines a Square class with size validation and area."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with an optional size."""
        self.size = size  
        """Initialize a new Square with an optional position."""
        self.position = position

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

    @property
    def position(self):
        """Get the current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, with validation"""
        if (not isinstance(value, tuple) or 
            len(value) != 2 or 
            not isinstance(value[0], int) or 
            not isinstance(value[1], int) or 
            value[0] < 0 or 
            value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print console the square"""
        if self.__size == 0:
            print()
        for b in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            print(" " * self.__position[0], end="")
            for k in range(0, self.__size):
                print("#", end="")
            print()
