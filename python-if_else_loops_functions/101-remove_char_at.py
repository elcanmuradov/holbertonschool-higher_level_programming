#!/usr/bin/python3

def remove_char_at(str, n):
    string = ""
    for i in str:
        if str.rinxdex(i) == n:
            string += i
    return string
