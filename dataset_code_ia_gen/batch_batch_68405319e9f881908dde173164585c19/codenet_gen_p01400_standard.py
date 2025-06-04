import sys
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0.0
    heap = [(0.0, start)]
    while heap:
        curr_d, u = heapq.heappop(heap)
        if dist[u] < curr_d:
            continue
        for v, time in graph[u]:
            nd = curr_d + time
            if dist[v] > nd:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

input=sys.stdin.readline
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    s,p,g=input().split()
    graph = {}
    nodes = set()
    for _ in range(m):
        a,b,d,t=input().split()
        d=int(d)
        t=int(t)
        time = d/40 + t
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, time))
        graph[b].append((a, time))
        nodes.add(a)
        nodes.add(b)
    # Dijkstra s->p
    dist_s = dijkstra(graph, s)
    # Dijkstra p->g
    dist_p = dijkstra(graph, p)
    ans = dist_s[p] + dist_p[g]
    print(int(ans))