def find(x):
  if par[x] == x:
    return x
  else:
    par[x] = find(par[x])
    return par[x]

def union(x, y):
  par_x = find(x)
  par_y = find(y)
  if rank[par_x] < rank[par_y]:
    par[par_x] = par_y
    w[par_y]+=w[par_x]
  else:
    par[par_y] = par_x
    w[par_x]+=w[par_y]
    if rank[par_x] == rank[par_y]:
      rank[par_x] += 1

def same(x, y):
  return find(x)==find(y)

def dfs(cur, prev):
  if visited[cur] or cur!=find(cur):
    while len(path)>0:
      union(0, path.pop())
    return
  visited[cur] = 1
  path.append(cur)
  for to in graph[cur]:
    if to==prev:
      continue
    dfs(to, cur)
  visited[cur] = 0
  if len(path)>0 and path[-1]==cur:
    path.pop()

def dfs2(cur):
  visited[cur] = 1
  ret = 0
  for i in range(len(graph2[cur])):
    for ele in graph[graph2[cur][i]]:
      if visited[find(ele)] == 0:
        ret = max(ret, dfs2(find(ele)))
  return ret+w[find(cur)]

import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
w = [0]
w.extend(list(map(int, input().split())))
graph = defaultdict(list)
for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

path = []
graph2 = [[] for _ in range(n+1)]
visited = [0]*(n+1)
par = [i for i in range(n+1)]
rank = [0]*(n+1)

dfs(1, -1)
for i in range(1, n+1):
  graph2[find(i)].append(i)

print(dfs2(find(1)))