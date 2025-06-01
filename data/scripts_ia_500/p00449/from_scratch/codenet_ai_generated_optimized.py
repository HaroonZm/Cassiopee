import sys
import heapq

input=sys.stdin.readline

while True:
    n,k=map(int,input().split())
    if n==0 and k==0:
        break

    graph=[[] for _ in range(n+1)]
    queries=[]
    edges_added=0

    for _ in range(k):
        line=input().split()
        if line[0]=='0':
            _,a,b=map(int,line)
            queries.append((a,b))
        else:
            _,c,d,e=map(int,line)
            graph[c].append((d,e))
            graph[d].append((c,e))
            edges_added+=1

    def dijkstra(start,end):
        dist=[float('inf')]*(n+1)
        dist[start]=0
        hq=[(0,start)]
        while hq:
            cost,u=heapq.heappop(hq)
            if dist[u]<cost:
                continue
            if u==end:
                return cost
            for v,w in graph[u]:
                nc=cost+w
                if dist[v]>nc:
                    dist[v]=nc
                    heapq.heappush(hq,(nc,v))
        return -1

    for a,b in queries:
        res=dijkstra(a,b)
        print(res)