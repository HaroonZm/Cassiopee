import sys
sys.setrecursionlimit(10**7)

def dfs(room, group, groups, graph):
    groups[room] = group
    for nxt, cost in graph[room]:
        if groups[nxt] == -1:
            dfs(nxt, group, groups, graph)

while True:
    line = sys.stdin.readline()
    if not line:
        break
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        x, y, c = map(int, sys.stdin.readline().split())
        graph[x].append((y, c))
        edges.append((x, y, c))

    groups = [-1] * n
    group_id = 0
    for i in range(n):
        if groups[i] == -1:
            dfs(i, group_id, groups, graph)
            group_id += 1

    # If all rooms are connected (only one group), then best is 0 cost or negative cost edges removal

    # But problem wants exactly two groups, both non-empty
    # Since we can remove any edges, including edges with negative cost
    # The minimal cost to separate into two groups is sum of costs of edges that go from one group to another
    # because by canceling all edges crossing groups, they can't move from group to another
    # So try all possible bipartitions? That's too hard for beginner

    # But the problem says:
    # "You have to decide two groups each room belongs to"
    # and "make impossible movement between groups"
    # To minimize cost, split nodes so that sum of crossing edges cost is minimum

    # A simple approach for beginner:
    # Since negative costs make canceling cheaper, cancel all edges with negative cost
    # Then check connectivity to find two groups:
    # We'll assign rooms reachable from 0 as group 0, rest as group 1
    # Calculate cost of crossing edges (edges from group0 to group1 or vice versa)
    # Output sum of their canceling cost

    # But since edges are one-way, moving only one direction matters.

    # Let's try:
    # Remove negative cost edges first (add their cost to answer)
    # Rebuild graph with remaining edges
    # Find rooms reachable from 0 - group 0, others group1
    # Sum cost of edges from group0 to group1 (those edges must be removed to separate)

    answer = 0
    filtered_edges = []
    for x,y,c in edges:
        if c < 0:
            answer += c  # canceling for negative cost edges is gain (reduce total cost)
        else:
            filtered_edges.append((x,y,c))

    graph2 = [[] for _ in range(n)]
    for x,y,c in filtered_edges:
        graph2[x].append(y)

    visited = [False]*n
    stack = [0]
    visited[0] = True
    while stack:
        cur = stack.pop()
        for nxt in graph2[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

    for x,y,c in filtered_edges:
        if visited[x] and not visited[y]:
            answer += c

    print(answer)