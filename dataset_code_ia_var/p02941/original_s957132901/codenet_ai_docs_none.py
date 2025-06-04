import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
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
n = I()
a = LI()
b = LI()
h = []
V = [0]*n
for i,v in enumerate(b):
    heappush(h,(-v,i))
    V[i] = v
ans = 0
while h:
    v,i = heappop(h)
    v = -v
    tmp = V[(i+1) % n] + V[i-1]
    if v == a[i]:
        continue
    s = (v - a[i])//tmp
    if s <= 0:
        print(-1)
        quit()
    ans += s
    v -= s*tmp
    V[i] = v
    if v != a[i]:
        heappush(h,(-v,i))
print(ans)