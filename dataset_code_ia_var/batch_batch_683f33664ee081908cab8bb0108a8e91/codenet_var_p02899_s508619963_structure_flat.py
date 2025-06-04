import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
from numba import njit
import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = range(1, N+1)
AB = zip(A, B)
sAB = sorted(AB)
l = list(sAB)
ans = []
for x in l:
    ans.append(x[1])
print(*ans)