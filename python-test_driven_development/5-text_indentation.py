#!/usr/bin/python3
"""
This module contains a function to print text with proper indentation.
It adds 2 new lines after '.', '?' and ':' characters.
The function also strips spaces from the beginning and end of each line.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':' characters.
    No spaces at the beginning or end of each printed line.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Process the text character by character
    i = 0
    while i < len(text):
        # Print current character
        print(text[i], end="")
        
        # Check if current character is one of the special characters
        if text[i] in ".?:":
            # Print 2 new lines
            print("\n")
            # Skip any spaces that follow
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            # Continue to next iteration (don't increment i again)
            continue
        
        i += 1