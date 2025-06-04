import sys
import heapq
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

S, R = map(int, input().split())
graph = [[] for _ in range(S+1)]
for _ in range(R):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

a,b,Q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

def dijkstra(start):
    dist = [float('inf')] * (S+1)
    dist[start] = 0
    hq = [(0,start)]
    while hq:
        cost, u = heapq.heappop(hq)
        if dist[u] < cost:
            continue
        for v,w in graph[u]:
            nd = cost + w
            if dist[v] > nd:
                dist[v] = nd
                heapq.heappush(hq, (nd,v))
    return dist

dist_a = dijkstra(a)
dist_b = dijkstra(b)

# Condition for a path p going from a -> ... -> c -> d -> ... -> b to be a shortest path from a to b:
# dist_a[b] == dist_a[c] + dist_c[d] + dist_d[b] with dist_c and dist_d distances from c and d respectively,
# and dist_c,d can be obtained from dist from c and d, but doing dijkstra Q times is too costly.
# But problem states the segment c-d must also be a shortest path between c and d.
# Check conditions:
# 1) dist_a[b] == dist_a[c] + dist_c[d] + dist_d[b]
# 2) The path from c-d is shortest: dist_c[d] == dist_d[c]

# To avoid multiple dijkstra, we compute dist from a and b.
# For distances between c and d: to check quickly, we compute dist from a and b only.
# Use dist_a and dist_b
# Note dist between c and d is NOT directly available.
# But we can compute dist from a and b and check if dist_a[b] == dist_a[c] + dist_c[d] + dist_d[b]
# Since dijkstra from c or d for each query would be expensive, but Q can be 40000, we can afford two dijkstra from c and d for each query? No.

# Alternative idea:
# If the graph is undirected and all edges positive, we can use Dijkstra.
# For shortest path, the triangle equality holds:
# dist_a[b] == dist_a[c] + dist_c[d] + dist_d[b]
# But again dist_c and dist_d not precomputed.

# Use the following equivalent condition given in solutions to similar problems:
# Path from a to b passing c, d in order and segment c-d is shortest path between c and d:
# Check dist_a[b] == dist_a[c] + dist_c[d] + dist_d[b], and
# dist_c[d] == dist_d[c]

# Since dist_c[d] symmetry, and undirected graph.

# To get dist_c[d], precompute dist from a and b is not enough.

# Alternative approach:
# For all vertices, precompute dist from a and b.
# For edge (u,v,w), if dist_a[u] + w + dist_b[v] == dist_a[b], then (u,v) can be on some shortest path from a to b.
# Similarly for (v,u,w).

# Build a shortest path DAG from a to b.

# Then, for query (c,d), check if there is a path from c to d along this DAG (meaning segment c-d is shortest path),
# and c and d are on some shortest path from a to b in order.

# So the plan:

# 1) Compute dist_a and dist_b.
# 2) Build DAG where edge u->v exists if dist_a[u] + w + dist_b[v] == dist_a[b].
# 3) For each query, check:
#   - dist_a[c] + dist_b[c] == dist_a[b] (c is on some shortest path)
#   - dist_a[d] + dist_b[d] == dist_a[b] (d is on some shortest path)
#   - There exists a path from c to d in DAG (so c before d)
# If all true, print Yes else No.

# To check path in DAG efficiently, we do a topological order of DAG and assign order indices.
# Then c can reach d if topo_order[c] <= topo_order[d] and there is path c->d.
# To check reachability quickly, we do reversed DAG and do BFS.

# Because the graph can be big, we do the following:

# For DAG:
# use adjacency list
# do DFS from a to get topo order (or use PQ)

# Then, for reachability from c to d, store for each vertex its topo order.
# Because DAG edges only go forward in topological order.
# Then if topo_order[c] > topo_order[d], no path c->d.

# But topo_order[c] <= topo_order[d] is necessary but not sufficient to ensure path.

# Then do BFS from c to check if d reachable in DAG.

# Since Q up to 40000 and each BFS is acceptable.

dist_a = dijkstra(a)
dist_b = dijkstra(b)
dist_ab = dist_a[b]

# Build DAG edges where edges are on shortest paths from a to b
dag = [[] for _ in range(S+1)]
for u in range(1,S+1):
    for v,w in graph[u]:
        if dist_a[u] + w + dist_b[v] == dist_ab:
            dag[u].append(v)
            
for c,d in queries:
    # check c and d on shortest path
    if dist_a[c] + dist_b[c] != dist_ab or dist_a[d] + dist_b[d] != dist_ab:
        print("No")
        continue
    # check reachable from c to d in dag
    if c == d:
        # c != d by problem statement, but just in case
        print("No")
        continue
    # quick check topo order? No precomputed topo order is needed, BFS is fine
    from collections import deque
    q = deque([c])
    visited = [False]*(S+1)
    visited[c] = True
    found = False
    while q:
        u = q.popleft()
        if u == d:
            found = True
            break
        for nx in dag[u]:
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
    print("Yes" if found else "No")