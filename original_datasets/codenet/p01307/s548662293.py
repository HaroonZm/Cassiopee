#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(10000000)

n = input()

for loop in range(n):
    S = map(int, list(raw_input()))
    cnt = 0
    while len(S) > 1:
        num = S[-1] + S[-2]
        if num >= 10:
            S[-2] = 1
            S[-1] = num % 10
        else:
            S[-2] = num
            S.pop()
        cnt += 1
    if cnt % 2 == 0:
        print "Audrey wins."
    else:
        print "Fabre wins."