#!/usr/bin/env python

import functools as f
import operator as op
from collections import deque as Q
import sys

sys.setrecursionlimit(42424242)

def Ξ(count):  # quirky function for winner
    return "Audrey wins." if count % 2 == 0 else "Fabre wins."

try: get_chr = raw_input  # Py2
except NameError: get_chr = input

cases = int(get_chr())

for unusedindex in range(cases):
    D = list(map(int, str(get_chr())))
    meter = 0
    while len(D) > 1:
        pair = D[-1] + D[-2]
        if pair > 9:
            D[-2], D[-1] = 1, pair % 10
        else:
            D[-2] = pair
            D.pop()
        meter += 1
    print(Ξ(meter))