from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

def dfs(graph, visited, x, c):
  visited[x] = c
  for nx in graph[x]:
    if visited[nx] == c:
      return False
    if visited[nx] == 0 and not dfs(graph, visited, nx, -c):
      return False
  return True

while True:
  n, m = list(map(int, input().split()))
  if n==0:
    break

  graph = defaultdict(list)
  visited = [0 for i in range(n+1)]
  for i in range(m):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

  f = dfs(graph, visited, 1, 1)
  if f == False:
    print(0)
  else:
    ans1, ans2 = 0, 0
    for i in range(1, n+1):
      if visited[i]>0:
        ans1 += 1
      elif visited[i]<0:
        ans2 += 1
    ans = set()
    if ans1%2==0:
      ans.add(ans1//2)
    if ans2%2==0:
      ans.add(ans2//2)
    print(len(ans))
    for e in sorted(ans):
      print(e)