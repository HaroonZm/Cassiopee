"""
AOJ 2608: Minus One

This script reads a graph (N nodes and M edges), performs Dijkstra's algorithm from two different nodes,
and computes a specific value based on shortest path distances. The code is annotated with detailed
comments and each function includes a comprehensive docstring.
"""

import heapq

MAX = 0x7fffffff  # An effective 'infinity' value for initial distances

def dijkstra(dist, start):
    """
    Compute shortest path distances from a starting node to all other nodes in an unweighted graph
    using a modified Dijkstra's algorithm.

    Args:
        dist (list[int]): A list where the shortest distances will be stored; initialized with MAX.
        start (int): The starting node index.

    Returns:
        None: The function updates the 'dist' list in place.
    """
    Q = []  # Priority queue to hold (distance_so_far, node)
    dist[start] = 0
    heapq.heappush(Q, (0, start))

    while Q:
        # Get the node with the smallest current distance
        t, s = heapq.heappop(Q)
        # If we already found a better path, ignore this one
        if dist[s] < t:
            continue
        # Explore all adjacent nodes
        for e in to[s]:
            nt = t + 1  # For unweighted graphs, all edges cost 1
            # If we found a shorter path to e, update the distance and push to queue
            if dist[e] > nt:
                dist[e] = nt
                heapq.heappush(Q, (nt, e))

# Read graph information: N (number of nodes), M (number of edges), s, t (start and end, 1-indexed)
N, M, s, t = map(int, input().split())
s, t = s-1, t-1  # Convert to 0-based indexing

# Initialize adjacency list for the graph
to = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x, y = x-1, y-1  # Convert to 0-based indexing
    to[x].append(y)
    to[y].append(x)  # Since the graph is undirected

# Compute shortest distances from s to every node
smin = [MAX] * N
dijkstra(smin, s)

# Compute shortest distances from t to every node
tmin = [MAX] * N
dijkstra(tmin, t)

# Count how many nodes are at distance d from s (scnt[d]), and from t (tcnt[d])
scnt = [0] * N
tcnt = [0] * N
for i in range(N):
    if smin[i] < N:
        scnt[smin[i]] += 1
    if tmin[i] < N:
        tcnt[tmin[i]] += 1

# Calculate the answer by considering node pairs whose shortest path is not minimal (minus one)
ans = 0
# The minimal path length from s to t
s_dist_to_t = smin[t] - 1
for i in range(s_dist_to_t):
    ans += scnt[i] * tcnt[s_dist_to_t - 1 - i]

print(ans)