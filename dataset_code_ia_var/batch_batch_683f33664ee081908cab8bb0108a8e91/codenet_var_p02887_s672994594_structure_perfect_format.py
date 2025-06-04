import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import numpy as np
import sys

sys.setrecursionlimit(10**7)

def _S():
    return sys.stdin.readline().rstrip()

def I():
    return int(sys.stdin.readline().rstrip())

def LI():
    return list(map(int, sys.stdin.readline().rstrip().split()))

def LS():
    return list(sys.stdin.readline().rstrip().split())

N = I()
S = _S()

last = ''
count = 0
for i in range(N):
    a = S[i]
    if last != a:
        count += 1
        last = a
print(count)