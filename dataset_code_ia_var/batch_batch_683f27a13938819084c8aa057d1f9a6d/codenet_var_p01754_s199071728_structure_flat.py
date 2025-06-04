import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**3
eps = 1.0 / 10**10
mod = 10**9+7

n_p_q = sys.stdin.readline().split()
n = int(n_p_q[0])
p = int(n_p_q[1])
q = int(n_p_q[2])
c = []
for _ in range(n):
    c.append(int(sys.stdin.readline()))
s = sum(c)
a = []
for i in range(n):
    a.append([c[i]+p*i, i])
a.sort()
r = s
for i in range(n):
    s -= c[a[i][1]] + p * a[i][1]
    t = s + p*i*(i+1) + p*q*(i+1)
    if t > r:
        r = t
print(r)