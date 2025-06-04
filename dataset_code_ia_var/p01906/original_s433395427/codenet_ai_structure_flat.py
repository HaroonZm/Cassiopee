import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])
a = list(map(int, input().split()))
r = 0
i = 0
while True:
    mi = ma = a[i % n]
    j = 1
    while j < m:
        t = a[(i + j) % n]
        if mi > t:
            mi = t
        elif ma < t:
            ma = t
        j += 1
    r += ma - mi
    i += m
    if i % n == 0:
        break
print(r)