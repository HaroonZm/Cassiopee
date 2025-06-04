import sys
import heapq

input=sys.stdin.readline

def build_fare_table(p, q, r):
    # Precompute fare for all distances up to max_distance=10000 (problem max)
    max_distance = 10000
    fare = [0]*(max_distance+1)
    idx = 1
    for i in range(1, max_distance+1):
        if idx < p and i > q[idx-1]:
            idx +=1
        fare[i] = fare[i-1] + r[idx-1]
    return fare

while True:
    n,m,c,s,g=map(int,input().split())
    if (n,m,c,s,g)==(0,0,0,0,0):
        break
    adj=[[] for _ in range(n+1)]
    for _ in range(m):
        x,y,d,comp=map(int,input().split())
        adj[x].append((y,d,comp))
        adj[y].append((x,d,comp))
    p = []
    q = []
    r = []
    for _ in range(c):
        pj=int(input())
        p.append(pj)
    for i in range(c):
        q.append(list(map(int,input().split())))
    for i in range(c):
        r.append(list(map(int,input().split())))
    fare_tables=[None]
    for i in range(c):
        fare_tables.append(build_fare_table(p[i], q[i], r[i]))
    # State: (cost_so_far, station, current_company, current_dist)
    # current_company: 0 means no current company (start or after switching)
    INF=10**15
    dist=[[ [INF]*(201) for __ in range(c+1)] for _ in range(n+1)]
    # at start, no company used, dist is 0 with dist 0
    dist[s][0][0]=0
    heap=[(0,s,0,0)]
    while heap:
        cost,u,ccurr,dcurr=heapq.heappop(heap)
        if dist[u][ccurr][dcurr]<cost:
            continue
        if u==g:
            print(cost)
            break
        for v,d,line_comp in adj[u]:
            if ccurr==line_comp:
                nd=(dcurr+d)
                add=0
                if nd>200:
                    # max dist stored is 200, to guarantee performance
                    nd=200
                ncost=cost
                # fare not added yet (only on switching or end)
                # Here we accumulate distance with same co
                if dist[v][ccurr][nd]>ncost:
                    dist[v][ccurr][nd]=ncost
                    heapq.heappush(heap,(ncost,v,ccurr,nd))
            else:
                add=0
                if d>200:
                    cost_d = fare_tables[line_comp][200]
                else:
                    cost_d = fare_tables[line_comp][d]
                ncost=cost
                # Add fare for old company section
                if ccurr!=0 and dcurr>0:
                    costold = fare_tables[ccurr][dcurr]
                    ncost+=costold
                ncost+=cost_d
                if dist[v][line_comp][d]>ncost:
                    dist[v][line_comp][d]=ncost
                    heapq.heappush(heap,(ncost,v,line_comp,d))
    else:
        # no break => no path
        print(-1)