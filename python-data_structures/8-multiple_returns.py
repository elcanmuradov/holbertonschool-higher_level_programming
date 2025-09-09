#!/usr/bin/python3

def multiple_returns(sentence):
    a = len(sentence)
    b = None if sentence == "" else sentence[0]
    return (a, b)
