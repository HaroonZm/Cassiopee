import sys
from collections import deque
from heapq import heappush,heappop

d = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs():
    dist = [[[float("inf")]*4 for i in range(w)] for j in range(h)]
    dist[0][0][0] = 0
    q = [(0,0,0,0)]
    while q:
        dn,y,x,c = heappop(q)
        for di in range(4):
            c_ = ro[di][c]
            y_ = y+d[c_][0]
            x_ = x+d[c_][1]
            if 0 <= y_ < h and 0 <= x_ < w:
                if dist[y_][x_][c_] > dn+co[y][x][di]:
                    dist[y_][x_][c_] = dn+co[y][x][di]
                    heappush(q,(dist[y_][x_][c_],y_,x_,c_))
    return dist

while 1:
    w,h = map(int, sys.stdin.readline().split())
    if w == 0:
        break
    s = [list(map(int, sys.stdin.readline().split())) for i in range(h)]
    cost = list(map(int, sys.stdin.readline().split()))
    co = [[[cost[i] for i in range(4)] for x in range(w)] for y in range(h)]
    for y in range(h):
        for x in range(w):
            if s[y][x] < 4:
                co[y][x][s[y][x]] = 0
    ro = [[0]*4 for i in range(4)]
    for c in range(4):
        for i in range(4):
            if c == 0:
                ro[c][i] = i
            elif c == 1:
                ro[c][i] = (i+1)%4
            elif c == 2:
                ro[c][i] = (i+2)%4
            else:
                ro[c][i] = (i+3)%4

    dist = bfs()
    print(min(dist[h-1][w-1]))