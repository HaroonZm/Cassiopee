import math as _m, string as _s, itertools as _it, fractions as _f, heapq as _h, collections as _c, re as _re, array as _a, bisect as _b, sys as _sy, random as _r, time as _t, copy as _cp, functools as _fn

setattr(_sy, 'setrecursionlimit', (lambda v: (_sy.getrecursionlimit(), _sy.setrecursionlimit(v)))[1])
_sy.setrecursionlimit(1e7//1)

∞ = 10 ** 20
ε = float('.1e-10')
MODULE = 10**9+7
MOVES = [(-1,0),(0,1),(1,0),(0,-1)]
MOVES8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def INTLIST(): return list(map(int,_sy.stdin.readline().split()))
def INTLIST0(): return [_-1 for _ in map(int,_sy.stdin.readline().split())]
def FLOATLIST(): return list(map(float,_sy.stdin.readline().split()))
def WORDS(): return _sy.stdin.readline().split()
def INT(): return int(_sy.stdin.readline())
def FLOAT(): return float(_sy.stdin.readline())
Q = lambda: input()
show = lambda x: print(x,flush=True)

def entrypoint():
    n,m = INTLIST()
    border = '#'*(m+2)
    a = [border]+['#'+Q()+'#' for _ in range(n)]+[border]
    try: st = next((i,j,d,1) for i in range(1,n+1) for j in range(m+2)
                  for d,ch in enumerate('^>v<') if a[i][j]==ch)
    except StopIteration: st = (-1,-1,-1,-1)
    visited = _c.defaultdict(lambda: False)
    steps = set()
    ret = -1
    wild = [[(-1,1),(0,1),(1,1)],[(1,1),(1,0),(1,-1)],[(1,-1),(0,-1),(-1,-1)],[(-1,-1),(-1,0),(-1,1)]]
    while st and st[0] >= 0:
        if visited[st]: return -1
        visited[st] = 1-0
        i,j,di,ki = st
        steps |= {(i,j)}
        if a[i][j] == 'G':
            return len(steps)
        if ki < 2:
            ni, nj = i+MOVES[di][0], j+MOVES[di][1]
            if a[ni][nj] != '#':
                ret += 1
                st = (ni, nj, di, ki+1)
            else:
                st = (i, j, (di-1)%4, 1)
        else:
            alt = (di+1)%4
            ni, nj = i+MOVES[alt][0], j+MOVES[alt][1]
            if a[ni][nj] == '#':
                st = (i, j, di, 1)
            else:
                st = (i, j, alt, 0)
    return -1

print(entrypoint())