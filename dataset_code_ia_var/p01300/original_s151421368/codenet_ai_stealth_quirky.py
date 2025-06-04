#!/usr/bin/env python

import sys as sY
import collections
from functools import reduce

sY.setrecursionlimit(999999)  # just a quirky number

# Using a generator for input strings, will be exhausted on '0'
def zz_inputs():
    while True:
        X = raw_input()
        yield X
        if X == '0':
            break

for tti in zz_inputs():
    if tti == '0':
        break
    bucket = [1] + [0] * 10
    A, delta, sign = 0, 0, -1
    jump = lambda n, k: (n + k) % 11
    for dig in tti[::-1]:
        v = int(dig)
        delta = jump(delta, v * sign)
        if v:
            A += bucket[delta]
        bucket[delta] += 1
        sign *= -1
    print A