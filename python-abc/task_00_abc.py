#!/usr/bin/python3
"""Abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
