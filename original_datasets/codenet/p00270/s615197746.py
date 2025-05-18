from heapq import heappush, heappop

s, r = map(int, input().split())
edges = [[] for _ in range(s)]
for _ in range(r):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, w))
    edges[v].append((u, w))

a, b, q = map(int, input().split())
a -= 1
b -= 1

def dijkstra(start):
    INF = 10 ** 20
    dist = [INF] * s
    dist[start] = 0
    parents = [[] for _ in range(s)]
    que = []
    heappush(que, (0, start))
    while que:
        score, node = heappop(que)
        for to, w in edges[node]:
            if dist[to] > score + w:
                dist[to] = score + w
                parents[to] = {node}
                heappush(que, (score + w, to))
            elif dist[to] == score + w:
                parents[to].add(node)
    return dist, parents

def on_shortest_path(c, d, mem):
    if c == d:return True
    if d in mem:return False
    mem.add(d)
    if dist_from_a[c] >= dist_from_a[d]:return False
    for parent in parents[d]:
        if on_shortest_path(c, parent, mem):return True
    return False

dist_from_a, parents = dijkstra(a)
dist_from_b, _ = dijkstra(b)
shortest = dist_from_a[b]
for _ in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist_from_a[c] + dist_from_b[c] == shortest and \
       dist_from_a[d] + dist_from_b[d] == shortest and \
       on_shortest_path(c, d, set()):
        print("Yes")
    else:
        print("No")