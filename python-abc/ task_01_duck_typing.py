#!/usr/bin/env python3
"""
This module demonstrates abstract base classes and duck typing with shapes.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A Circle class that inherits from Shape."""

    def __init__(self, radius):
        """
        Initialize a Circle with radius.

        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle (π * r²)
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.

        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing.

    This function relies on duck typing - it assumes the passed object
    has area() and perimeter() methods, without explicitly checking
    the object's type or inheritance.

    Args:
        shape: Any object that implements area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
