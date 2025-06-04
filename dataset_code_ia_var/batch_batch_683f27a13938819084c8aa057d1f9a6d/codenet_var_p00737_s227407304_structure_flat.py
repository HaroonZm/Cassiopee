import sys
from heapq import heappush, heappop

d = [(0,1),(1,0),(0,-1),(-1,0)]

while 1:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0:
        break
    s = []
    for i in range(h):
        s.append(list(map(int, sys.stdin.readline().split())))
    cost = list(map(int, sys.stdin.readline().split()))
    co = []
    for y in range(h):
        row = []
        for x in range(w):
            row.append([cost[i] for i in range(4)])
        co.append(row)
    for y in range(h):
        for x in range(w):
            if s[y][x] < 4:
                co[y][x][s[y][x]] = 0
    ro = []
    for c in range(4):
        row = []
        for i in range(4):
            if c == 0:
                row.append(i)
            elif c == 1:
                row.append((i+1)%4)
            elif c == 2:
                row.append((i+2)%4)
            else:
                row.append((i+3)%4)
        ro.append(row)
    dist = [[[float("inf")]*4 for _ in range(w)] for _ in range(h)]
    dist[0][0][0] = 0
    q = [(0,0,0,0)]
    while q:
        dn, y, x, c = heappop(q)
        for di in range(4):
            c_ = ro[di][c]
            y_ = y + d[c_][0]
            x_ = x + d[c_][1]
            if 0 <= y_ < h and 0 <= x_ < w:
                if dist[y_][x_][c_] > dn + co[y][x][di]:
                    dist[y_][x_][c_] = dn + co[y][x][di]
                    heappush(q, (dist[y_][x_][c_], y_, x_, c_))
    print(min(dist[h-1][w-1]))