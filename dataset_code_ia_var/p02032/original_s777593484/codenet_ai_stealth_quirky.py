import sys as _s
_s.setrecursionlimit(9**6+77)
from collections import deque as dq

getter = lambda: [*map(int, input().split())]

def _allPrimeUpTo(M):
    fl = [True]*(M+1)
    fl[0]=fl[1]=False
    xb = []
    i = 1
    while i < M:
        i += 1
        if fl[i]:
            xb += [i]
            for z in range(i*2, M+1, i):
                fl[z] = False
    return xb

X = int(input())
all_p = _allPrimeUpTo(1000010)
z=[0]*len(all_p)
idx=0
while idx<len(all_p):
    y=all_p[idx]
    while not X%y:
        z[idx]+=1
        X//=y
    idx+=1

z+=[X-1!=0]
foo = [v!=0 for v in z]
A = sum(foo)
B = 1
i_=0
while i_ < len(z):
    B *= (z[i_]+1)
    i_+=1
B -= 1
print(A, B)