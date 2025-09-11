#!/usr/bin/python3

def change_number(num):
    if num == 'I':
        return 1
    elif num == 'V':
        return 5
    elif num == 'X':
        return 10
    elif num == 'L':
        return 50
    elif num == 'C':
        return 100
    elif num == 'D':
        return 500
    elif num == 'M':
        return 1000
    else:
        return -1
    
# LXXXVII
def roman_to_int(roman_string):
    if roman_string is None or roman_string is int:
        return None
    number = 0
    if len(roman_string) == 1:
        return change_number(roman_string)
    else:
        for i in range(0, len(roman_string) - 2):
            if change_number(roman_string[i]) >= change_number(roman_string[i + 1]):
                number += change_number(roman_string[i])
            else:
                number -= change_number(roman_string[i])
        if change_number(roman_string[len(roman_string) - 1]) <= change_number(roman_string[len(roman_string) - 2]):
            number += change_number(roman_string[len(roman_string) - 1])
        else:
            number -= change_number(roman_string[len(roman_string) - 2])
        return number        
