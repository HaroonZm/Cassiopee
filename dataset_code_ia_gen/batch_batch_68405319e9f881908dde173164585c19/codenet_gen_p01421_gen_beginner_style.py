from collections import deque

N, M = map(int, input().split())
edges = []
graph = [[] for _ in range(N)]
for i in range(M):
    X, Y = map(int, input().split())
    edges.append((X-1, Y-1))
S, T = map(int, input().split())
S -= 1
T -= 1

# We try all subsets of edges to reverse (not efficient but simple)
# Since M can be up to 1000, exhaustive is impossible
# So we do a heuristic:
# - Build graph with original edges forward and reversed edges also available but with capacity 0
# - Assign capacity 1 for edges in original direction, and capacity 0 for reversed edges
# - We try to improve flow by increasing capacity on reversed edges by reversing the edge once
# Here, as beginner, we will:
# - Initially set capacity 1 for all edges in original direction
# - Also add reverse edges with capacity 0
# - Try to find max flow
# - Then try for each edge:
#     reverse direction (set original capacity 0, reversed capacity 1)
#     find max flow again
#     keep if flow improves
# This is O(M * max_flow), which can be slow but acceptable for small input

# Build initial capacity matrix
capacity = [[0]*N for _ in range(N)]
for i, (x,y) in enumerate(edges):
    capacity[x][y] = 1

def bfs(cap, s, t, parent):
    visited = [False]*N
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v in range(N):
            if not visited[v] and cap[u][v] > 0:
                visited[v] = True
                parent[v] = u
                if v == t:
                    return True
                queue.append(v)
    return False

def max_flow(cap, s, t):
    flow = 0
    parent = [-1]*N
    while bfs(cap, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, cap[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            cap[u][v] -= path_flow
            cap[v][u] += path_flow
            v = u
        flow += path_flow
    return flow

# Compute initial max flow
cap_init = [row[:] for row in capacity]
flow_init = max_flow(cap_init, S, T)

best_flow = flow_init
best_reversed = []

# Try reversing edges one by one, keep track of improvements
# We will try to reverse multiple edges greedily
reversed_set = set()
while True:
    improved = False
    for i, (x,y) in enumerate(edges):
        if i in reversed_set:
            continue
        # Try reversing edge i
        cap_try = [row[:] for row in capacity]
        # reverse edge i
        cap_try[x][y] = 0
        cap_try[y][x] = 1
        # Also apply already reversed edges
        for r in reversed_set:
            rx, ry = edges[r]
            cap_try[rx][ry] = 0
            cap_try[ry][rx] = 1

        flow_try = max_flow([row[:] for row in cap_try], S, T)
        if flow_try > best_flow:
            best_flow = flow_try
            reversed_set.add(i)
            improved = True
            break
    if not improved:
        break

print(best_flow)
print(len(reversed_set))
for i in reversed_set:
    print(i+1)