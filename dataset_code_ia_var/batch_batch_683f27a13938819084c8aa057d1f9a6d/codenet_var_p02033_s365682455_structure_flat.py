from collections import defaultdict
from heapq import heappush, heappop
import sys
import math
import bisect
import random

mod = 1000000007

n,m = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))
f = [0]*(n+1)
i = 1
while i < m:
    f[a[i]-a[i-1]-1] += 1
    i += 1
f[n-a[-1]] += 1
s = 0
k = [0]*(n+1)
i = n-1
while i >= 0:
    s += f[i]
    k[i] += s + k[i+1]
    i -= 1
i = 0
while i < n+1:
    k[i] += a[0]-1
    i += 1
q = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
for v in p:
    l = 0
    r = n
    while r-l > 1:
        m = (l+r)//2
        if k[m] > v:
            l = m
        else:
            r = m
    if k[r] > v:
        print(-1)
    else:
        print(r)