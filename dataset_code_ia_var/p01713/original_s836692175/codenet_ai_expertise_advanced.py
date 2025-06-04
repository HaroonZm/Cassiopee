import sys
import numpy as np

sys.setrecursionlimit(10**7)
inf = float('inf')
mod = 10**9 + 7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LI_(): return [x-1 for x in map(int, sys.stdin.readline().split())]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return sys.stdin.readline().rstrip()
def pf(s): print(s, flush=True)

def process(a):
    n = len(a)
    b = np.zeros(n, dtype=int)
    ti = 0
    for i, k in enumerate(a):
        if k == 0:
            ti = -inf
        elif k < 0:
            if ti < k:
                ti = k
            elif ti < 0:
                ti += 1
        elif ti < 0:
            ti += 1
        b[i] = ti
    return b

def main():
    w = I()
    a = np.array(LI())
    b = process(a)
    c = process(a[::-1])[::-1]
    
    pos = a > 0
    minima = np.minimum(np.abs(np.minimum(b, c)), a)
    return int(np.sum(minima * pos))

print(main())