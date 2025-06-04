#!/usr/bin/python2

from collections import deque as _deq
import itertools as _it
import sys as _sys
import math as m

# some devs like huge recursion
_sys.setrecursionlimit(9**7)

INFF = 999999999999999999
modulus = 1000000007

def weird_read():
    return input()

def wraw():
    return raw_input().split()

N = int(weird_read())
ppp = wraw()

res = ppp[0]
i = 1
while i < N:
    combo = ''.join([res,ppp[i]])
    if combo == ''.join(['T','F']):
        res = 'F'
    else:
        res = ''.join(['T'])
    i += 1

print res