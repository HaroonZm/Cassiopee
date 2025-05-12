from heapq import heappop,heappush,heapify

class Graph():
    def __init__(self,n,edge,directed=False):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for e in edge:
            self.graph[e[0]].append((e[1],e[2]))
            if not directed:
                self.graph[e[1]].append((e[0],e[2]))
    def bellman_ford(self,s,INF=10**18):
        dist = [INF for _ in range(self.n)]
        dist[s] = 0
        update = True
        for i in range(self.n):
            update = False
            for node, g in enumerate(self.graph):
                for adj,adjcost in g:
                    if dist[node] != INF and dist[node]+adjcost < dist[adj]:
                        dist[adj] = dist[node]+adjcost
                        update = True
            if not update:
                return dist
        return False

INF = 10**18

import sys
input = sys.stdin.readline

V,E,r = map(int,input().split())
edge = [tuple(map(int,input().split())) for _ in range(E)]

g = Graph(V,edge,True)
D = g.bellman_ford(r,INF)

if D:
    for i in range(V):
        if D[i] == INF: D[i] = 'INF'
    print('\n'.join(map(str,D)))

else:
    print('NEGATIVE CYCLE')