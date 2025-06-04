from functools import reduce
from itertools import product, count, chain
from collections import deque as dq

def getdelta():
    return list(zip(*[iter([0,1,0,-1,1,0,-1,0])]*2))[:4]
Δ = getdelta()

def split_ints(s):
    return list(map(int, s.split()))
    
h, w = split_ints(input())
field = []
for _ in range(h):
    field.append(input())

def const_grid(val, h, w):
    return [[val for _ in range(w)] for _ in range(h)]

pdist, sdist = map(lambda _: const_grid(1000, h, w), (0,1))
pque, sque = map(dq, ((),()) )

def locations(field, targets):
    return ((i, j, c) for i, row in enumerate(field) for j, c in enumerate(row) if c in targets)

meta = {'@': None, '$': [], '%': None}
for i, j, c in locations(field, {'@', '$', '%'}):
    if c == '@':
        pque.append((i,j))
        pdist[i][j] = 0
        meta['@'] = (i, j)
    if c == '$':
        sque.append((i,j))
        sdist[i][j] = 0
        meta['$'].append((i,j))
    if c == '%':
        meta['%'] = (i, j)

def BFS(q, dmat, cond=lambda *_: True, crit=lambda x: x+1):
    while q:
        i,j = q.popleft()
        for di,dj in Δ:
            ni, nj = i+di, j+dj
            if 0 <= ni < h and 0 <= nj < w:
                if all((field[ni][nj] != '#', dmat[ni][nj] > crit(dmat[i][j]))):
                    if cond(ni, nj, dmat, i, j):
                        dmat[ni][nj] = crit(dmat[i][j])
                        q.append((ni, nj))

BFS(sque, sdist)
BFS(pque, pdist, cond=lambda ni, nj, d, pi, pj: pdist[ni][nj] > pdist[pi][pj]+1 and pdist[pi][pj]+1 < sdist[ni][nj], crit=lambda x: x+1)

val = reduce(lambda a,b: a if a < b else b, [pdist[meta['%'][0]][meta['%'][1]], 1000-1])
print(("No","Yes")[val < 1000])