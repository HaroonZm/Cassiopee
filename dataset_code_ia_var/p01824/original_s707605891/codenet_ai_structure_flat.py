import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

a,b,c,n = [int(x) for x in sys.stdin.readline().split()]
aa = []
for _ in range(n):
    aa.append([int(x) for x in sys.stdin.readline().split()])
r = (a*b+b*c+c*a) * 2

for i in range(n):
    d,e,f = aa[i]
    r += 6
    if d == 0:
        r -= 2
    if e == 0:
        r -= 2
    if f == 0:
        r -= 2
    if d == a-1:
        r -= 2
    if e == b-1:
        r -= 2
    if f == c-1:
        r -= 2

for i in range(n):
    ai = aa[i]
    for j in range(i+1,n):
        aj = aa[j]
        if abs(ai[0]-aj[0]) + abs(ai[1]-aj[1]) + abs(ai[2]-aj[2]) == 1:
            r -= 2

print(r)