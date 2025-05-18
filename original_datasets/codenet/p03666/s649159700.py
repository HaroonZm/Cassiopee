#!/usr/bin/env python3
#AGC17 B

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n,a,b,c,d = LI()

f = defaultdict(list)
lst = []
s,t = 0,n-1
for _ in range(n):
    lst.append((a+s*c-t*d,a+s*d-t*c))
    s += 1
    t -= 1
for i,j in lst:
    if i <= b <= j:
        print('YES')
        quit()
print('NO')