#!/usr/bin/python3

def change_number(num):
    match num:
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000
        case _:
            return -1
    
# LXXXVII
def roman_to_int(roman_string):
    number = 0
    if len(roman_string) == 1:
        return change_number(roman_string)
    else:
        for i in range(0, len(roman_string) - 1):
            if change_number(i) >= change_number(i + 1):
                number += change_number(i)
            else:
                number -= change_number(i)
        if change_number(roman_string[len(roman_string) - 1]) <= change_number(roman_string[len(roman_string) - 2]):
            number += change_number(roman_string[len(roman_string) - 1])
        else:
            number -= change_number(roman_string[len(roman_string) - 2])
        return number        
