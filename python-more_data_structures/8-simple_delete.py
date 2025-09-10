#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary is None or key is None:
        return
    return a_dictionary.pop(key)