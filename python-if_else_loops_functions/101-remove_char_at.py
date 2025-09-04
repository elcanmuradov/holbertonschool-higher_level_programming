#!/usr/bin/python3

def remove_char_at(str, n):
    c = 0
    for i in str:
        c += 1
    if n < c:
        str = list(str)
        str.pop(n)
        string = "".join(str)
        return string
    else:
        return str
