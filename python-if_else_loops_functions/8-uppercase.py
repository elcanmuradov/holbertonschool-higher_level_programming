#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        # if lowercase letter a-z, convert to uppercase A-Z
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
