from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect

sys.setrecursionlimit(1000000)
mod = 1000000007

bl = bisect.bisect_left
br = bisect.bisect_right

n = int(sys.stdin.readline())
p = []
for _ in range(n):
    p.append([int(x) for x in sys.stdin.readline().split()])

fx = set()
for x1, y1, x2, y2 in p:
    fx.add(x1)
    fx.add(x2)
fx = list(fx)
fx.sort()

fy = set()
for x1, y1, x2, y2 in p:
    fy.add(y1)
    fy.add(y2)
fy = list(fy)
fy.sort()

h = len(fy)
w = len(fx)
a = []
for i in range(h):
    a.append([0]*w)

for x1, y1, x2, y2 in p:
    l = bl(fx, x1)
    u = bl(fy, y1)
    r = bl(fx, x2)
    d = bl(fy, y2)
    a[u][l] += 1
    a[u][r] -= 1
    a[d][l] -= 1
    a[d][r] += 1

s = []
for i in range(h):
    s.append(list(accumulate(a[i])))

for j in range(w):
    for i in range(h-1):
        s[i+1][j] += s[i][j]

ans = 0
for i in range(h-1):
    y = fy[i+1] - fy[i]
    for j in range(w-1):
        if s[i][j]:
            x = fx[j+1] - fx[j]
            ans += x * y
print(ans)