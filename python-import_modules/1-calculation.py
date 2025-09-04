#!/usr/bin/python3

from calculation_1 import sub
from calculation_1 import div
from calculation_1 import mul
from calculation_1 import add

if __name__ == "__main__":
    a = 10
    b = 5
    print("{} + {} = {}\n".format(a, b, add(a, b)))
    print("{} - {} = {}\n".format(a, b, sub(a, b)))
    print("{} * {} = {}\n".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
