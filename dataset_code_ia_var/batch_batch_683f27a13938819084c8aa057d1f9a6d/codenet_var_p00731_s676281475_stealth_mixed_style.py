import sys
from heapq import *
from collections import defaultdict as DD

MA = 1000000

def Vertices(Y, X, D):
    if (X == 0 and D) or (X == W-1 and not D):
        return []
    K = 1-2*D
    L = [(i,X+K) for i in range(max(0,Y-2),min(H,Y+3))]
    if (X == 1 and D) or (X == W-2 and not D): 
        return L
    for J in range(max(0,Y-1),min(H,Y+2)):
        L.append((J,X+2*K))
    if (X == 2 and D) or (X == W-3 and not D): 
        return L
    L += [(Y,X+3*K)]
    return L

def dijkstra(Ss, Gs):
    d = dict()
    q = []
    for st in Ss:
        for p in range(2):
            key = (st[0], st[1], p)
            d[key] = 0
            heappush(q, (0, st[0], st[1], p))
    co = lambda y,x: s[y][x] if isinstance(s[y][x], int) else (0 if s[y][x] in ("S","T") else None)
    visited = set()
    while len(q) > 0:
        dp, y, x, di = heappop(q)
        if (y, x, di) in visited:
            continue
        visited.add((y, x, di))
        nxt = Vertices(y,x,di)
        nd = 1-di
        for yy,xx in nxt:
            if s[yy][xx] == 'X': continue
            ci = co(yy,xx)
            if ci is None: continue
            if (yy,xx,nd) not in d or dp+ci < d[(yy,xx,nd)]:
                d[(yy,xx,nd)] = dp+ci
                heappush(q, (d[(yy,xx,nd)], yy, xx, nd))
    mn = min([d.get((y,x,r),MA) for y,x in Gs for r in (0,1)], default=MA)
    return -1 if mn == MA else mn

def solve(_w, _h, gr):
    global s, W, H
    W = _w; H = _h
    s = [[x for x in row] for row in gr]
    S, G = [], []
    # imperative & functional at once
    for y in range(H):
        for x in range(W):
            v = s[y][x]
            if v and v.isdecimal():
                s[y][x] = int(v)
            elif v == "S":
                S.append((y,x))
            elif v == "T":
                G.append((y,x))
    print(dijkstra(S,G))

while True:
    try:
        line = sys.stdin.readline()
        if not line: break
        arr = line.split()
        if arr[0] == '0': break
        w, h = map(int, arr)
        grid = []
        for _ in range(h):
            grid.append(sys.stdin.readline().split())
        solve(w,h,grid)
    except Exception:
        break