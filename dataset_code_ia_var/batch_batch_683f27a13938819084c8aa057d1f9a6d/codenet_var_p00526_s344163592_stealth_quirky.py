# AOJ 0603 Illumination - Non-conventional style

import sys as _S
from sys import stdin as _SD
_READ = lambda: _SD.readline()

def __(_): return list(map(int, _READ().split()))
N = int(_READ())
A = __(_S)
K=[];x=1
for I in range(1,N):
    if A[I]!=A[I-1]:
        K+=[x]
        x=1
    else:x+=1
K+=[x] if N else None

M=Q=0
for j,e in enumerate(K):
    Q+=e
    Q-=K[j-3] if j>2 else 0
    M=M if M>Q else Q
print(M)