from heapq import heappush, heappop
INF = 10 ** 20
n, m, x = map(int, input().split())
tlst = [int(input()) for _ in range(n)]
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, d))
    edges[b].append((a, d))
que = []
heappush(que, (0, x, x, 0))
dic = {}
dic[(x, x, 0)] = 0
while que:
    total, ct, ht, node = heappop(que)
    if dic.get((ct, ht, node), INF) < total:
        continue
    for to, dist in edges[node]:
        new_ct = max(0, ct - dist)
        new_ht = max(0, ht - dist)
        t = tlst[to]
        if t == 1 or (t == 0 and new_ht == 0) or (t == 2 and new_ct == 0):
            new_total = total + dist
            if t == 0:
                new_ct = x
            if t == 2:
                new_ht = x
            if dic.get((new_ct, new_ht, to), INF) > new_total:
                dic[(new_ct, new_ht, to)] = new_total
                heappush(que, (new_total, new_ct, new_ht, to))
ans = INF
for ct in range(x + 1):
    for ht in range(x + 1):
        if (ct, ht, n - 1) in dic and dic[(ct, ht, n - 1)] < ans:
            ans = dic[(ct, ht, n - 1)]
print(ans)