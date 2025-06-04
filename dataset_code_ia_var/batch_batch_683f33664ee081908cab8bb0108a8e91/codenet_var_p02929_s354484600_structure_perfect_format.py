import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import copy
import functools
import random
import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop
from itertools import permutations, combinations, product, accumulate, groupby
from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig

sys.setrecursionlimit(10 ** 7)

inf = 10 ** 20
INF = float("INF")
ans = 1
tmp = 0
cnt = 0
ansli = []
tmpli = []
candili = []
stillset = set()
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ddn9 = ddn + [(0, 0)]

def wi():
    return list(map(int, sys.stdin.readline().split()))

def wip():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def ws():
    return sys.stdin.readline().split()

def i():
    return int(sys.stdin.readline())

def s():
    return input()

def s_list():
    return list(input())

def hi(n):
    return [i() for _ in range(n)]

def hs(n):
    return [s() for _ in range(n)]

def mi(n):
    return [wi() for _ in range(n)]

def num_grid(n):
    return [[int(i) for i in sys.stdin.readline().split()[0]] for _ in range(n)]

def mip(n):
    return [wip() for _ in range(n)]

def ms(n):
    return [ws() for _ in range(n)]

def grid(n):
    return [s_list() for _ in range(n)]

n = i()
s = s()
new_s = ""
for idx in range(2 * n):
    if (2 * n - idx - 1) % 2 == 0:
        new_s += s[idx]
    else:
        new_s += "W" if s[idx] == "B" else "B"

lr = ""
for idx in range(2 * n):
    if new_s[idx] == "B":
        lr += "R"
    else:
        lr += "L"

if lr.count("R") != n:
    print(0)
    exit()

lcount = 0
for idx in range(2 * n):
    if lr[idx] == "L":
        lcount += 1
    else:
        ans *= lcount
        ans %= mod
        lcount -= 1

for j in range(1, n + 1):
    ans *= j
    ans %= mod

print(ans)