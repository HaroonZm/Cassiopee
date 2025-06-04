import sys
from collections import deque

# Mr. Endo's BFS code keeps track of 'current' set but does not mark visited nodes.
# We want to know if this process will ever reach the full set of vertices exactly,
# and if yes, after how many iterations.

# Key insights:
# - The graph is connected.
# - The 'current' set evolves by replacing current with the set of neighbors of vertices in current.
# - Because visited is not stored, nodes can appear and disappear in 'current' set over iterations.
# - We want to detect if this process stabilizes and reaches all vertices, or cycles infinitely without reaching all.
#
# Approach:
# 1. Represent sets of vertices as frozenset to store and detect cycles.
# 2. Start from current = {1}.
# 3. Repeatedly:
#    - Compute found = union of neighbors of vertices in current.
#    - current = found
#    - Check:
#      * if current == set of all vertices => return iteration count (stop condition)
#      * if current has been seen before => cycle detected => result -1
#
# Complexity:
# - Each iteration requires to:
#   * iterate over all vertices in current
#   * for each, get adjacency list neighbors
# - Storing visited states as frozensets for large sets can be expensive:
#   But we can keep a set of bitsets or hashes of sets for detection.
#
# Optimization:
# - Use a visited set of frozenset or strings
# - Given constraints, using frozenset is feasible with hashing
#
# The key problem is that sets can be large, but since the graph is connected,
# and the sets evolve deterministically, loops or convergence can be detected quickly.

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

all_vertices = frozenset(range(1, N + 1))
current = frozenset([1])

seen_states = set()
seen_states.add(current)

iterations = 0
while True:
    iterations += 1
    found_set = set()
    # For each vertex in current, add its neighbors to found_set
    for v in current:
        for u in graph[v]:
            found_set.add(u)
    current = frozenset(found_set)

    if current == all_vertices:
        # Mr. Endo's code will stop after 'iterations' loops
        print(iterations)
        break
    if current in seen_states:
        # Cycle detected, infinite loop without stopping
        print(-1)
        break
    seen_states.add(current)