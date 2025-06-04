from heapq import heappush, heappop

INF = 10 ** 20
while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    edges = [[] for _ in range(n * 2)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append((b, c))
        edges[a + n].append((b + n, c))
        edges[b].append((a, c))
        edges[b + n].append((a + n, c))
    for i in range(n):
        adds = []
        for to, _ in edges[i]:
            if to < n:
                for toto, _ in edges[to]:
                    if toto < n and toto != i:
                        adds.append((toto + n, 0))
        edges[i].extend(adds)
    edges[n - 1].append((2 * n - 1, 0))
    costs = [INF] * (2 * n)
    que = []
    heappush(que, (0, 0))
    while que:
        total, node = heappop(que)
        for to, cost in edges[node]:
            if costs[to] > total + cost:
                costs[to] = total + cost
                heappush(que, (total + cost, to))
    print(costs[2 * n - 1])