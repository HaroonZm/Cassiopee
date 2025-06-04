import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# For each cell i, we jump from i to (i + a[i]) % N
# We want to know how many starting positions can eventually reach the starting cell after some moves.

# We can model this as a graph with each node having exactly one outgoing edge.
# The problem reduces to finding how many nodes belong to cycles that can be reached from themselves.

# We'll do DFS with coloring:
# 0: unvisited
# 1: visiting
# 2: visited and on a cycle
# 3: visited but cannot reach a cycle that returns to start

color = [0]*N

def dfs(u):
    if color[u] == 1:
        # Found a cycle
        color[u] = 2
        return u
    if color[u] > 1:
        return -1
    color[u] = 1
    v = (u + a[u]) % N
    res = dfs(v)
    if res == -1:
        color[u] = 3
        return -1
    else:
        color[u] = 2
        if u == res:
            return -1
        else:
            return res

for i in range(N):
    if color[i] == 0:
        dfs(i)

# Count how many nodes are in color 2 (can reach a cycle that returns to itself)
print(color.count(2))