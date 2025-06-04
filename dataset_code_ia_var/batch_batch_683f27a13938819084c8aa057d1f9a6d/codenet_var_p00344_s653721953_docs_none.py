import sys
sys.setrecursionlimit(1000000)
n = int(input())
alst = list(map(int, input().split()))
edges = [[] for _ in range(n)]
rev_edges = [[] for _ in range(n)]
for i in range(n):
  edges[i].append((i + alst[i]) % n)
  rev_edges[(i + alst[i]) % n].append(i)
def dfs(x, ret, edges, visited):
  visited[x] = True
  for e in edges[x]:
    if not visited[e]:
      dfs(e, ret, edges, visited)
  ret.append(x)
def dfs_rev(x, cycles, rev_edges, visited):
  visited[x] = True
  flag = False
  for e in rev_edges[x]:
    if not visited[e]:
      cycles.add(e)
      dfs_rev(e, cycles, rev_edges, visited)
      flag = True
    elif x == e:
      flag = True
  if flag:
    cycles.add(x)
order = []
visited = [False] * n
for i in range(n):
  if not visited[i]:
    dfs(i, order, edges, visited)
order.reverse()
visited = [False] * n
cycles = set()
for i in order:
  if not visited[i]:
    dfs_rev(i, cycles, rev_edges, visited)
print(len(cycles))