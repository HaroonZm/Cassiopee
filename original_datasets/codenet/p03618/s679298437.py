import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
MOD = 10**9+7

A = input().rstrip()
d = defaultdict(int)
for i in range(len(A)):
    d[A[i]] += 1
    
s = 0
for k in d.keys():
    s += d[k]

ans = 0
for k in d.keys():
    s -= d[k]
    ans += d[k]*s
print(ans+1)