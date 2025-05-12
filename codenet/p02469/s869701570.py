#!/usr/bin/env python

"""
input:
4
1 2 3 5

output:
30
"""

import sys
from functools import reduce
from operator import mod

def gcd(x, y):
    if x < y:
        x, y = y, x

    while y > 0:
        r = mod(x, y)
        x = y
        y = r

    return x

def lcm(a, b):
    return a * b // gcd(a, b)

def solve(_n_list):
    return reduce(lcm, _n_list)

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    cnt = int(_input[0])
    n_list = tuple(map(int, _input[1].split()))
    print(solve(n_list))