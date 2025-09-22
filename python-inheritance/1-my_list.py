#!/usr/bin/python3
"""Module that defines an an object"""


class MyList(list):
    """Class the defines new list"""
    def __init__(self, newList=[]):
        """Initialize a new list"""
        self.newList = newList

    """Print the sorted list """
    def print_sorted(self):
        print(sorted(self))
