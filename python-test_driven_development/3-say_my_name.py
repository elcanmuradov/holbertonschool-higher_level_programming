#!/usr/bin/python3
"""
This module contains a function to print a name.
It handles validation for first and last name parameters.
The function prints "My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".
    Both parameters must be strings.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the formatted name
    print("My name is {} {}".format(first_name, last_name))