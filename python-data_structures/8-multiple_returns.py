#!/usr/bin/python3

def multiple_returns(sentence):
    a = len(sentence) if sentence != None else 0
    b = sentence[0] if sentence != None else None
    return (a, b)