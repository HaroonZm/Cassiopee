from heapq import heappush, heappop

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    s, p, g = input().split()
    edges = {}
    for _ in range(m):
        a, b, d, t = input().split()
        if a not in edges:
            edges[a] = []
        if b not in edges:
            edges[b] = []
        d = int(d)
        t = int(t)
        edges[a].append((b, d // 40 + t))
        edges[b].append((a, d // 40 + t))

    INF = 10 ** 20

    def score(start, goal):
        dist = {name: INF for name in edges.keys()}
        dist[start] = 0
        que = []
        heappush(que, (0, start))
        while que:
            total, name = heappop(que)
            if name == goal:
                return total
            for to, cost in edges[name]:
                if dist[to] > total + cost:
                    dist[to] = total + cost
                    heappush(que, (total + cost, to))

    print(score(s, p) + score(p, g))