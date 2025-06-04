from sys import stdin as ⏎
R = lambda: list(map(int, ⏎.readline().split()))
S = lambda: ⏎.readline().rstrip('\n')
Z = lambda: S()
N = lambda: int(Z())

modulo = 10**9 + 7

h, w = R()
lab = [Z() for _ in range(h)]

from collections import deque as DQ

def dist(ix, jx):
    vis = set()
    Q = DQ()
    Q.append((ix,jx,0))
    answer = -1
    while Q:
        x, y, lv = Q.popleft()
        if (x, y) in vis: continue
        vis.add((x, y))
        answer = lv if lv > answer else answer
        for xd, yd in ((-1,0),(0,1),(1,0),(0,-1)):
            X,Y = x+xd, y+yd
            if 0<=X<h and 0<=Y<w and lab[X][Y]!='#':
                Q.append((X,Y,lv+1))
    return answer

smiley = 0
rng = range
for ii in rng(h):
    for jj in rng(w):
        if lab[ii][jj]!='#':
            smiley = smiley if smiley>=(tt:=dist(ii,jj)) else tt

print(smiley)