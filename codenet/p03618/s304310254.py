from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

s = input()
n = len(s)
c = Counter(s)
cnt = 0
for key,value in c.items():
    if value >= 2:
        cnt += value*(value-1)//2
print(n*(n-1)//2 - cnt + 1)