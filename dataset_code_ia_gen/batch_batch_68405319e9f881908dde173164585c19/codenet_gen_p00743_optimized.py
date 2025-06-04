import sys
import math
import heapq

input=sys.stdin.readline

while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    s,g=map(int,input().split())
    edges=[[] for _ in range(n+1)]
    for _ in range(m):
        x,y,d,c=map(int,input().split())
        edges[x].append((y,d,c))
        edges[y].append((x,d,c))
    # state: (city, speed, prev_city)
    # speed from 1 to max 30 (speed limit max)
    # prev_city from 0 to n (0 means start no prev)
    # We'll do Dijkstra on (city,speed,prev_city)
    INF=float('inf')
    dist=[[[INF]*(n+1) for _ in range(31)] for __ in range(n+1)]
    # initial: at start city s, prev_city=0(no prev), speed=1 before going on first road, but speed applies on roads not cities
    # The car must run first road at speed=1, so for first move we start at s with no speed yet.
    # We'll model initial moves by pushing all edges from s with speed=1 only.
    # So initial states: from s, speed=1, prev_city=0, dist=0. Will relax neighbors accordingly.
    # Actually, to include speed from arrivals, we must push a dummy state at s with speed=0 and prev=0 and cost=0, then from s generate speed=1 edges.
    pq=[]
    for v in range(31):
        for p in range(n+1):
            dist[s][v][p]=INF
    dist[s][0][0]=0.0
    heapq.heappush(pq,(0.0,s,0,0)) #(cost, city, speed, prev_city)
    while pq:
        cost,u,v,pv=heapq.heappop(pq)
        if dist[u][v][pv]<cost:
            continue
        # If reached goal city g at speed=1 (speed on last road must be 1)
        # Actually, arrival at g must be at speed=1 edge, so state is city=g and speed=1, prev_city can be any.
        if u==g and v==1:
            print(f'{cost:.5f}')
            break
        for w,d,c in edges[u]:
            if w==pv:
                continue
            # from city u, came with speed v, can leave with speed nv in {v-1,v,v+1} if in range [1..c]
            for nv in [v-1,v,v+1]:
                if nv<1 or nv>c:
                    continue
                # on first move: if v=0 means initial position, must leave at speed 1 only
                if v==0 and nv!=1:
                    continue
                ncost=cost+d/nv
                if dist[w][nv][u]>ncost:
                    dist[w][nv][u]=ncost
                    heapq.heappush(pq,(ncost,w,nv,u))
    else:
        print("unreachable")