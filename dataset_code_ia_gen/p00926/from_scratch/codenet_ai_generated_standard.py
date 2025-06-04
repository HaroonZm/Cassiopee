import sys
sys.setrecursionlimit(10**7)

N, m = map(int, input().split())
constraints = [tuple(map(int, input().split())) for _ in range(m)]

# Build graph for dependencies reversed: edge from d to c means c after d
graph = [[] for _ in range(N+1)]
for c, d in constraints:
    graph[d].append(c)

visited = [False]*(N+1)
order = []

def dfs(u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
    order.append(u)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
order.reverse()  # Topological order

pos = [0]*(N+1)
min_pos = N+1
max_pos = 0

for shop in order:
    pos[shop] = shop
    min_pos = min(min_pos, shop)
    max_pos = max(max_pos, shop)

# She starts at entrance (0), visits all shops with constraints between min_pos and max_pos,
# possibly more shops outside this range can be visited without affecting constraints,
# but to minimize distance, only shops in the segment [min_pos, max_pos] are needed to be traveled.
# Since she can visit other shops in any order, minimal walking is from 0 to min_pos,
# then to max_pos, then to exit (N+1).

res = 0
if m == 0:
    # No constraints, just go straight from 0 to N+1
    res = N+1
else:
    # Distance from entrance to leftmost constrained shop
    res += min_pos
    # Distance between leftmost and rightmost constrained shops
    res += max_pos - min_pos
    # Distance from rightmost constrained shop to exit
    res += (N+1) - max_pos

print(res)