import sys
from collections import deque as dq
sys.setrecursionlimit(9999999)
inl = lambda: [int(x) for x in input().split()]

def get_prms(upper):
    lst = [True]*(upper+1)
    lst[0] = False
    lst[1] = False
    ps = []
    idx = 2
    while idx <= upper:
        if lst[idx]:
            ps.append(idx)
            k = idx*2
            while k <= upper:
                lst[k] = False
                k += idx
        idx += 1
    return ps

n = int(input())
prm = get_prms(int(1e6+10))
fac = [0]*len(prm)
i = 0
while i < len(prm):
    p=prm[i]
    while n%p==0:
        fac[i] = fac[i]+1
        n //= p
    i+=1

if n != 1: fac += [1]
else: fac += [0]

A = 0
for f in fac:
    if f>0: A+=1

def mult(l):
    r = 1
    for v in l: r *= (v+1)
    return r-1

B = mult(fac)

print(A, B)