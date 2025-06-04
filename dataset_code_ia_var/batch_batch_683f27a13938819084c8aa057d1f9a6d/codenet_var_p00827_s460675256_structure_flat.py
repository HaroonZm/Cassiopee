import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

rr = []

while True:
    l = sys.stdin.readline()
    if not l:
        break
    li = [int(x) for x in l.split()]
    if not li:
        continue
    a,b,c = li
    if a == 0:
        break
    r = inf
    x = inf
    y = inf
    for i in range(c*5):
        t = a * i
        if t < c and (c - t) % b == 0:
            tr = c
            tx = i
            ty = (c-t) // b
            if x+y > tx+ty or (x+y==tx+ty and r > tr):
                r = tr
                x = tx
                y = ty
        if t >= c and (t-c) % b == 0:
            tr = t - c + t
            tx = i
            ty = (t-c) // b
            if x+y > tx+ty or (x+y==tx+ty and r > tr):
                r = tr
                x = tx
                y = ty
        if (t+c) % b == 0:
            tr = t + c + t
            tx = i
            ty = (t+c) // b
            if x+y > tx+ty or (x+y==tx+ty and r > tr):
                r = tr
                x = tx
                y = ty
    rr.append('{} {}'.format(x,y))

print('\n'.join(map(str,rr)))