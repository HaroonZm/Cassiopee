from sys import stdin
from itertools import chain

def neighbors(y, x):
    for dy, dx in ((1,0), (0,1), (-1,0), (0,-1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w:
            yield ny, nx

h, w = map(int, stdin.readline().split())
g = [list(map(int, stdin.readline().split())) for _ in range(h)]
pos = [None] * (h * w)
for i, row in enumerate(g):
    for j, val in enumerate(row):
        pos[val-1] = (i, j)

stop = [set() for _ in range(h * w)]
ans = 0
for idx, (y, x) in enumerate(pos):
    for ny, nx in neighbors(y, x):
        if g[ny][nx] < g[y][x]:
            stop[idx].update(stop[g[ny][nx]-1])
    cnt = len(stop[idx])
    if cnt >= 2:
        ans += 1
    elif cnt == 0:
        stop[idx].add(g[y][x])

print(ans)