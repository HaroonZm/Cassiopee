#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

while True:
    S = raw_input()
    if S == '0':
        break
    m = {}
    for i in range(11):
        m[i] = []
    m[0].append(11)
    diff = 0
    even = True
    S = reversed(S)
    for c in S:
        num = int(c)
        if even:
            diff += num
        else:
            diff -= num
        diff %= 11
        m[diff].append(num)
        even = (not even)
    ans = 0
    #print m
    for i in range(11):
        lst = m[i]
        for i in range(len(lst)):
            if lst[i] != 0:
                ans += i
    
    print ans