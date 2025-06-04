import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Début du code principal excessivement plat

n = int(sys.stdin.readline())
a = [0]
for i in range(1, 50000):
    a.append(a[-1] + i)

t = bisect.bisect_left(a, n)
r = [1] * t + [0] * t
for i in range(t):
    ai = a[t-i]
    ti = t + i
    if n < ai:
        ts = min(t, ai-n)
        r[ti],r[ti-ts] = r[ti-ts],r[ti]
        n -= t - ts
    else:
        break

print(''.join(map(lambda x: '()'[x], r)))