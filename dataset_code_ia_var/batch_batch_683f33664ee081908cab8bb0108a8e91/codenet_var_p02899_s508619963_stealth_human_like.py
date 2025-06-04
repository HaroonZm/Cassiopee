import bisect
import collections
import copy
import heapq
import itertools
import math
import string

import numpy as np
from numba import njit # hmm, not sure if needed
import sys

sys.setrecursionlimit(10000000) # just in case things go deep

def _S(): 
    return sys.stdin.readline().rstrip()

def I():
    return int(sys.stdin.readline().rstrip())

def LI(): 
    return list(map(int, sys.stdin.readline().rstrip().split()))

def LS(): 
    # strings in list from stdin, that's it
    return list(sys.stdin.readline().rstrip().split())

N = I()
A = LI()
B = list(range(1, N+1)) # prefer lists personally
AB = zip(A, B)
# print(AB) # just checking

sAB = sorted(AB)
# print(sAB) # debugging

_an, ans = zip(*sAB)
print(*ans) # hope this works

# some ideas for future me:
# AB = [LI() for _ in range(N)]
# A, B = zip(*AB)
# Ap = np.array(A)
# C = np.zeros(N + 1) # why plus one, old me?
# index 順 要素のindex

# attempt to remake the ans in a dumb way
# ans2 = []
# for i in range(N):
#     ans2.append(A.index(i+1)+1)
# print(*ans2)

# Eh, the numpy stuff isn't really needed here? Oh well.