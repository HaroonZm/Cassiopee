from heapq import heappush, heappop

INF = 10 ** 20

n, m, k, s = map(int, input().split())
p, q = map(int, input().split())

z_dist = [INF] * n
que = []

for _ in range(k):
    c = int(input()) - 1
    z_dist[c] = 0
    heappush(que, (0, c))

edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

while que:
    total, node = heappop(que)
    for to in edges[node]:
        if z_dist[to] > total + 1:
            z_dist[to] = total + 1
            heappush(que, (total + 1, to))

cost = [INF] * n
cost[0] = 0
que = []
heappush(que, (0, 0))

while que:
    total, node = heappop(que)
    for to in edges[node]:
        if to == n - 1:
            if cost[to] > total:
                cost[to] = total
            continue
        if z_dist[to] == 0:
            continue
        if z_dist[to] <= s:
            price = q
        else:
            price = p
        if cost[to] > total + price:
            cost[to] = total + price
            heappush(que, (total + price, to))

print(cost[n - 1])