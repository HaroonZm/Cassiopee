def find(parent, x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(parent, rank, x, y):
    rx = find(parent, x)
    ry = find(parent, y)
    if rx != ry:
        if rank[rx] < rank[ry]:
            parent[rx] = ry
        else:
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1
        return True
    return False

while True:
    line = input().strip()
    if not line:
        continue
    n, m = map(int, line.split())
    if n == 0 and m == 0:
        break
    edges = []
    for _ in range(m):
        s, t, c = map(int, input().split())
        edges.append((c, s, t))
    edges.sort(key=lambda x: x[0])
    # number of edges in spanning tree = n-1
    # median index = (n-1)//2 since n is even, n-1 is odd
    median_index = (n - 1) // 2

    # Try all spanning trees obtained by edges in some range [i...j]
    # and find the minimal median of costs
    # since median is the middle in sorted order, if we consider edges between edges[i] to edges[j],
    # the median is edges[i + median_index]
    # So we just try all possible i with i + median_index < len(edges)
    # and try to build spanning tree with edges between i and i+median_index + k for k>=0
    # since we try to minimize median, we can fix median edge and see if can build spanning tree with edges >= median edge and <= some bound

    # A simple approach:
    # For each i:
    #   Let median_edge = edges[i + median_index]
    #   Try to build spanning tree using edges from edges[i] to edges[m-1] (edges with cost at least edges[i])
    #   If possible, record median = median_edge[0]
    # Take minimal among those.

    answer = None
    total_edges = len(edges)
    for i in range(total_edges - median_index):
        low = i
        median_edge = edges[i + median_index]
        # Build spanning tree with edges cost >= edges[low][0] and cost <= median_edge[0]
        # Actually edges are sorted increasing, so edges[low] <= median_edge, so edges[low to whatever that <= median_edge]
        # But edges are sorted, median_edge is edges[i + median_index], so edges from i to i+median_index have costs <= median_edge cost
        # So we can take edges from i to end, try to build spanning tree with edges cost between edges[i][0] and median_edge[0]
        # So edges with cost in [edges[i][0], median_edge[0]]
        # Let's collect those edges
        cost_min = edges[i][0]
        cost_med = median_edge[0]
        candidate_edges = [e for e in edges if cost_min <= e[0] <= cost_med]

        parent = [j for j in range(n+1)]
        rank = [0]*(n+1)
        count = 0
        for c, s, t in candidate_edges:
            if union(parent, rank, s, t):
                count += 1
            if count == n - 1:
                break
        if count == n - 1:
            if answer is None or cost_med < answer:
                answer = cost_med

    print(answer)