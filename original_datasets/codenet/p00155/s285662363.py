from heapq import heappush, heappop

INF = 10 ** 20

while True:
  n = int(input())
  if n == 0:break

  buil_point = [None] * n
  for _ in range(n):
    b, x, y = map(int, input().split())
    buil_point[b - 1] = (x, y)
  
  edges = [[] for _ in range(n)]
  for i in range(n):
    for j in range(i + 1, n):
      ix, iy = buil_point[i]
      jx, jy = buil_point[j]
      cost = ((jx - ix) ** 2 + (jy - iy) ** 2) ** (1 / 2)
      if cost <= 50:
        edges[i].append((cost, j))
        edges[j].append((cost, i))

  m = int(input())
  for _ in range(m):
    s, g = map(int, input().split())
    costs = [INF] * n
    costs[s - 1] = 0
    paths = [[]] * n
    paths[s - 1] = [s - 1]
    que = []
    heappush(que, (0, [s - 1]))
    while que:
      dist, path = heappop(que)
      last = path[-1]
      for cost, to in edges[last]:
        if costs[to] > dist + cost:
          costs[to] = dist + cost
          paths[to] = path + [to]
          heappush(que, (dist + cost, path + [to]))
    
    if paths[g - 1]:
      print(*list(map(lambda x:x + 1, paths[g - 1])))
    else:
      print("NA")