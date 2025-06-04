import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(0,-1),(1,0),(0,1),(-1,0)]
ddn = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

# Lecture de n et s
n = int(sys.stdin.readline())
s = input()

# Construction de a
a = [2]
for i in range(n):
    if s[i] == '>':
        a.append(None)
    else:
        a.append(1)
a.append(2)

# Recherche du max par binaire + simulation linéaire
ma = n+1
mi = 0
mm = (ma+mi)//2
r = 0

while ma > mi:
    mm = (ma+mi)//2
    # bloc de code à la place de la fonction f(mm)
    i = mm
    if i < 0 or i > n+1:
        c, ff = 0, None
    else:
        c = 0
        nl = i-1
        nr = i+1
        ni = i
        while a[ni] != 2:
            if a[ni] is None:
                ni = nr
                nr += 1
            else:
                ni = nl
                nl -= 1
            c += 1
        ff = (ni == 0)
    if r < c:
        r = c
    if ff:
        mi = mm + 1
    else:
        ma = mm

for i in range(mm-1, mm+2):
    if i < 0 or i > n+1:
        c, ff = 0, None
    else:
        c = 0
        nl = i-1
        nr = i+1
        ni = i
        while a[ni] != 2:
            if a[ni] is None:
                ni = nr
                nr += 1
            else:
                ni = nl
                nl -= 1
            c += 1
        ff = (ni == 0)
    if r < c:
        r = c

print(r)