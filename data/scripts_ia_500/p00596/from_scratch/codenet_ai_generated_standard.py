from sys import stdin
from collections import defaultdict, deque

def can_arrange(dominoes):
    graph = defaultdict(list)
    degree = defaultdict(int)
    edges_count = 0

    # Build undirected multigraph
    for d in dominoes:
        a, b = d
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1
        edges_count += 1

    # Check connectivity over vertices with edges
    vertices = [v for v in degree if degree[v] > 0]
    if not vertices:
        return True  # empty or single domino

    visited = set()
    def dfs(u):
        visited.add(u)
        for w in graph[u]:
            if w not in visited:
                dfs(w)

    dfs(vertices[0])
    if any(v not in visited for v in vertices):
        return False

    # Count vertices with odd degree
    odd_deg = sum(1 for v in degree if degree[v] % 2 == 1)
    return odd_deg == 0 or odd_deg == 2

lines = [line.strip() for line in stdin if line.strip()]
for i in range(0, len(lines), 2):
    n = int(lines[i])
    if n == 0:
        print("Yes")
        continue
    raw = lines[i+1].split()
    dominoes = []
    for r in raw:
        if len(r) == 2:
            a, b = int(r[0]), int(r[1])
            dominoes.append((a,b))
    print("Yes" if can_arrange(dominoes) else "No")