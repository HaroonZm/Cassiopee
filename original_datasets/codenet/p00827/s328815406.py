#!/usr/bin/env python

from collections import deque
import itertools as it
import sys
import math

while True:
    A, B, C = map(int, raw_input().split())
    if A + B + C == 0:
        break
    lst = []
    for i in range(10001):
        if (C + A * i) % B == 0:
            num = (C + A * i) / B
            lst.append((i + num, A * i + B * num, i))
        if (C - A * i) % B == 0:
            num = (C - A * i) / B
            if num < 0:
                num *= -1
            lst.append((i + num, A * i + B * num, i))
    lst.sort()
    print str(lst[0][2]) + ' ' + str(lst[0][0] - lst[0][2])