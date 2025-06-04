from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

sys.setrecursionlimit(1000000)
mod = 998244353

# Lecture des entrées
line = sys.stdin.readline()
n, k, a = [int(x) for x in line.split()]

lst = [0]*(k+1)
lst[-2] = 1
A = a * pow(100*n, mod-2, mod)
inv = pow(n, mod-2, mod)

i = k-2
while i >= 0:
    if k > i + n:
        val = (A * (lst[i+1] - lst[i+n+1]) + lst[i+1]) % mod
        lst[i] = val
    else:
        val = (A * (lst[i+1] - lst[k]) + (n-(k-i)+1)*inv + lst[i+1]) % mod
        lst[i] = val
    i -= 1

print((lst[0] - lst[1]) % mod)