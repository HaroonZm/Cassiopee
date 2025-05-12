from heapq import heappush, heappop

INF = 10 ** 20

while True:
  n, m, l = map(int, input().split())
  if n == 0:
    break
  edges = [[] for _ in range(n * (l + 1))]
  for _ in range(m):
    a, b, d, e = map(int, input().split())
    a -= 1
    b -= 1
    for i in range(d, l + 1):
      edges[i * n + a].append((0, (i - d) * n + b))
      edges[i * n + b].append((0, (i - d) * n + a))
    for i in range(l + 1):
      edges[i * n + a].append((e, i * n + b))
      edges[i * n + b].append((e, i * n + a))
  
  que = []
  heappush(que, (0, l * n))
  costs = [INF] * (n * (l + 1))
  costs[l * n] = 0
  while que:
    total, node = heappop(que)
    for enemy, to in edges[node]:
      if costs[to] > total + enemy:
        costs[to] = total + enemy
        heappush(que, (total + enemy, to))

  ans = min(costs[i * n + n - 1] for i in range(l + 1))
  print(ans)