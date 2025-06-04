import bisect, collections, copy, heapq, itertools, math, string
import numpy as np
import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

last = ''
count = 0
i = 0
while i < N:
    a = S[i]
    if last != a:
        count += 1
        last = a
    i += 1
print(count)