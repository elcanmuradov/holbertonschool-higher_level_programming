#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return
    temp = 0
    for i in a_dictionary.keys:
        if temp < a_dictionary[i]:
            temp = a_dictionary[i]
    return temp
