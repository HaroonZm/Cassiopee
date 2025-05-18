def bfs(x, visited, order):
  if visited[x]:
    return
  visited[x] = True
  for to in edges[x]:
    bfs(to, visited, order)
  order.append(x)

def bfs_rev(x):
  if visited[x]:
    return []
  visited[x] = True
  ret = [x]
  for to in rev_edges[x]:
    ret += bfs_rev(to)
  return ret

n = int(input())
edges = [[] for _ in range(200)]
rev_edges = [[] for _ in range(200)]
for _ in range(n):
  u, s, d = input().split()
  u = int(u) - 1
  d = int(d) - 1 + 100
  if s == "lock":
    edges[d].append(u)
    rev_edges[u].append(d)
  else:
    edges[u].append(d)
    rev_edges[d].append(u)

order = []
visited = [False] * 200
for i in range(200):
  if not visited[i]:
    bfs(i, visited, order)

order.reverse()
visited = [False] * 200
for i in order:
  if not visited[i]:
    if len(bfs_rev(i)) >= 2:
      print(1)
      break
else:
  print(0)