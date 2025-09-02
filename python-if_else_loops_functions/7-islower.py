#!/usr/bin/python3
def islower(c):
    if not isinstance(c, str) or len(c) != 1:
        raise TypeError("Expected a single character string")
    if "a" <= c <= "z":
        return True
    else:
        return False
