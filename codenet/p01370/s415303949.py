#!/usr/bin/env python

import heapq as hq

def bfs(x,y,t,Map):
    queue = []
    hq.heappush(queue,(0,(x,y)))
    while len(queue) != 0:
        p = hq.heappop(queue)
        x,y = p[1]
        if p[0] <= t and Map[y][x] == 0:
            Map[y][x] = 1
            dxdy = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]
            for dx,dy in dxdy:
                hq.heappush(queue,(p[0] + 1, (x + dx, y + dy)))

while True:
    t,n = map(int,input().split())
    if t == 0 and n == 0:
        break

    Map = [[0 for j in range(200)] for i in range(200)]
    for _ in range(n):
        x,y = map(lambda x:int(x) + 100,input().split())
        Map[y][x] = -1
    x,y = map(lambda x:int(x) + 100,input().split())
    bfs(x,y,t,Map)

    print(sum([0 if Map[i][j] == -1 else Map[i][j] for i in range(200) for j in range(200)]))