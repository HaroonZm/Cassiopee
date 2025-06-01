from collections import deque

def make_DAG(start, n, graph):
    # Creating adjacency list for DAG
    new_graph = [[] for _ in range(n)]
    dist = [float('inf')] * n
    dist[start] = 0
    dq = deque([start])
    visited = [False] * n
    visited[start] = True
    indeg = [0] * n

    while dq:
        current = dq.popleft()
        for nxt in graph[current]:
            # Only extend if this path is shorter or equal
            if dist[nxt] >= dist[current] + 1:
                if not visited[nxt]:
                    visited[nxt] = True
                    dq.append(nxt)
                new_graph[current].append(nxt)
                dist[nxt] = dist[current] + 1
                indeg[nxt] += 1
    return new_graph, dist, indeg

def bfs_count(s, DAG, indeg):
    indeg[s] -= 1
    if indeg[s] != 0:
        return 0
    dq = deque([s])
    count = 1
    while dq:
        now = dq.popleft()
        for nxt in DAG[now]:
            # skipping edges we've already accounted for
            if (now, nxt) in ok:
                continue
            ok[(now, nxt)] = True
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                count += 1
                dq.append(nxt)
    return count


n, m, q = map(int, raw_input().split())
edges = []
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, raw_input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
    edges.append((u, v))

DAG, dist, indeg = make_DAG(0, n, g)
ans = 0
ok = {}

for _ in range(q):
    r = int(raw_input()) - 1
    u, v = edges[r]
    if abs(dist[u] - dist[v]) == 0:
        # no point in adding anything if same level
        print ans
        continue
    if dist[u] < dist[v]:
        if (u, v) not in ok:
            ok[(u, v)] = True
            ans += bfs_count(v, DAG, indeg)
    else:
        if (v, u) not in ok:
            ok[(v, u)] = True
            ans += bfs_count(u, DAG, indeg)
    print ans