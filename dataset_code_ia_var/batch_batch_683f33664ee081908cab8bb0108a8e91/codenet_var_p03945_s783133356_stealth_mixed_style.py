import sys as s; import re as _re
from collections import deque as dq, Counter as Cnt, defaultdict
from math import ceil, sqrt
import math
from functools import reduce; import heapq
import itertools
from copy import copy
from operator import itemgetter as ig
from string import ascii_letters; from bisect import bisect_left as bisl
INF = float('inf')
MOD = 1000000007

# Input shorthands
read = lambda: s.stdin.readline().rstrip()
def INT(): return int(read())
def MAP(): return map(int, read().split())
def LIST(): return [int(x) for x in read().split()]
getzip = lambda n: zip(*(MAP() for _ in range(n)))

s.setrecursionlimit(10**9)

S = read()
cnt = 0

i=1
while i < len(S):
    if S[i] != S[i-1]:
        cnt+=1
    i+=1

print(cnt)