import sys
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

S,R = map(int,input().split())
graph = [[] for _ in range(S+1)]
for _ in range(R):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
a,b,Q = map(int,input().split())

def dijkstra(start):
    dist = [float('inf')] * (S+1)
    dist[start] = 0
    hq = [(0,start)]
    while hq:
        cd,c = heapq.heappop(hq)
        if dist[c]<cd:
            continue
        for nx,w in graph[c]:
            nd = cd + w
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(hq,(nd,nx))
    return dist

dist_a = dijkstra(a)
dist_b = dijkstra(b)

#Precompute dist from all nodes to a and b is heavy, use dist_a and dist_b only

# Condition 1: path p is shortest from a to b, so dist_a[b] is the shortest distance a-b
ab_dist = dist_a[b]

for _ in range(Q):
    c,d = map(int,input().split())
    # Check if there's a shortest a-b path passing through c then d, with c-d path shortest
    # Conditions:
    # 1) dist_a[c] + dist from c to d + dist_b[d] == dist_a[b]
    # 2) dist from c to d is shortest path distance
    # For dist from c to d, use dist_c from dijkstra from c
    # To optimize, note that dist_a[c] + dist_a[b] must be known.
    # We'll run dijkstra from c only once per query is expensive, so we precompute all pair shortest distances? Too big.
    # So we run dijkstra from c only when needed then cache. But Q can be 40000
    # Better: since the graph is fixed, we can run dijkstra from all query c's? MAYBE heavy
    # Alternative: for c-d shortest distance, we can check dijkstra from c to d on demand.
    # Since constraints are big, we can process all queries before and run dijkstra from all unique c's.
    # Collect all c and d pairs first
import collections
queries = [tuple(map(int,input().split())) for _ in range(Q)]

unique_nodes = set()
for c,d in queries:
    unique_nodes.add(c)
dist_cache = {}
for c in unique_nodes:
    dist_c = dijkstra(c)
    dist_cache[c] = dist_c

for c,d in queries:
    dist_c = dist_cache[c]
    if dist_a[c]==float('inf') or dist_b[d]==float('inf') or dist_c[d]==float('inf'):
        print('No')
        continue
    if dist_a[c] + dist_c[d] + dist_b[d] == ab_dist:
        print('Yes')
    else:
        print('No')