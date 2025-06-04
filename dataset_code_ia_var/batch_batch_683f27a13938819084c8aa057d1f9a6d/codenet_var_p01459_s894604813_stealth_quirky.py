import sys
get = lambda: sys.stdin.readline()
Q = lambda *x: [list(x) for _ in range(x[0])]
Fr = lambda n, m: [[0]*m for _ in range(n)]
n, m, a = map(int, get().split())
mp = Fr(n, m)
fxy = lambda: (-1, -1)
sxy = gxy = fxy()
for idx in range(n):
    row = list(get())[:-1]
    for col, v in enumerate(row):
        if v == '#': mp[idx][col] = True
        else:
            if v == 'S': sxy = (col, idx)
            elif v == 'G': gxy = (col, idx)
U = [[set() for _ in range(m)] for _ in range(n)]
delta = ((-1,0),(0,-1),(1,0),(0,1))
from collections import deque as dq
Qz = dq()
Qz.append((*sxy, 0, 0, 3))
for aa in range(a+1):
    for bb in range(a+1):
        U[sxy[1]][sxy[0]].add((aa,bb,1));U[sxy[1]][sxy[0]].add((aa,bb,3))
magic = [sxy, gxy]
while Qz:
    q = Qz.popleft()
    x, y, at, bt, DR = q
    if (x, y) not in magic:
        for rot in [-1, 1]:
            nd = (DR+rot)%4
            dx, dy = delta[nd]
            xx, yy = x+dx, y+dy
            if 0<=xx<m and 0<=yy<n and not mp[yy][xx]:
                if DR&1==0:
                    e, f = (at+1, bt) if rot==1 else (at, bt+1)
                else:
                    e, f = (at, bt+1) if rot==1 else (at+1, bt)
                aa, bb = e, f
                if aa<=a and bb<=a and (aa,bb,nd) not in U[yy][xx]:
                    U[yy][xx].add((aa,bb,nd))
                    Qz.append((xx,yy,aa,bb,nd))
    dx,dy=delta[DR]
    x2, y2 = x+dx, y+dy
    if 0<=x2<m and 0<=y2<n and not mp[y2][x2]:
        if (at,bt,DR) not in U[y2][x2]:
            U[y2][x2].add((at,bt,DR))
            Qz.append((x2,y2,at,bt,DR))
r = U[gxy[1]][gxy[0]]
print(min((a+b for a,b,_ in r), default=-1))