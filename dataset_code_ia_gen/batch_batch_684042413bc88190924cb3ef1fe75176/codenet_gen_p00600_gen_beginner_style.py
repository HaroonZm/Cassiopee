while True:
    s, d = map(int, input().split())
    if s == 0 and d == 0:
        break
    # Read distances between hot springs and districts
    hot_dists = []
    for _ in range(s):
        hot_dists.append(list(map(int, input().split())))
    # Read distances between districts
    district_dists = []
    for i in range(d - 1):
        district_dists.append(list(map(int, input().split())))

    # Build graph: vertices 0 to s-1 are hot springs, s to s+d-1 are districts
    n = s + d
    edges = []
    for i in range(s):
        for j in range(d):
            dist = hot_dists[i][j]
            if dist != 0:
                edges.append((dist, i, s + j))
    for i in range(d - 1):
        for j in range(d - i - 1):
            dist = district_dists[i][j]
            if dist != 0:
                u = s + j
                v = s + i + j + 1
                edges.append((dist, u, v))

    # Use a simple Union-Find structure to find MST
    parent = [i for i in range(n)]
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def unite(a,b):
        a = find(a)
        b = find(b)
        if a != b:
            parent[b] = a
            return True
        return False

    edges.sort(key=lambda x: x[0])
    res = 0
    # MST must connect all districts and at least one hot spring as start point
    # Actually, problem states the pipeline starts from some hot spring and connects all districts
    # so MST over all nodes (hot springs and districts) is fine
    for dist, u, v in edges:
        if unite(u,v):
            res += dist

    print(res)