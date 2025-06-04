import sys
import math
import itertools as it
from collections import deque
from functools import reduce
from operator import xor

sys.setrecursionlimit(int(1e8))

def hexstr(x): return hex(x)[2:]

def next9():
    q=deque()
    while len(q)<9:
        q.extend(map(lambda z:int(z,16), input().split()))
    return list(q)

def conj(a, b): return (a + (1 << 32) - b) % (1 << 32)

def expand(lst,res):
    mask=1<<32
    f=lambda i:sum((1<<i if not (x&(1<<i)) else -(1<<i)) for x in lst+[(mask-1)^res])%mask
    return [(f(i),1<<i) for i in range(32)]

def halven(seq,off=0):
    base=[(off,0)]
    for v in seq:
        base += list(map(lambda p:((p[0]+v[0])%(1<<32),p[1]+v[1]), base))
    return base

def min_pair(L):
    L=sorted(L)
    if L[0][0]==0: return hexstr(L[0][1])
    return None

N=int(input())
for _ in range(N):
    buf=next9()
    val=buf[8]
    source=buf[:8]
    d=conj(sum(source),val)
    difs=expand(source,val)
    a,b=halven(difs[:16],d),halven(difs[16:])
    if (r:=min_pair(a)):
        print(r)
        continue
    ak, bk = sorted(a), sorted(b)
    i,j = 0,len(bk)-1
    found = False
    while i<len(ak) and j>=0 and not found:
        s = ak[i][0]+bk[j][0]
        if s==(1<<32):
            print(hexstr(ak[i][1]+bk[j][1]))
            found=True
        elif s>(1<<32):
            j-=1
        else:
            i+=1