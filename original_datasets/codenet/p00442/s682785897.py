import sys
sys.setrecursionlimit(100000)
V, E = int(input()), int(input())
L = []
visited = [0 for i in range(V)]
edges = [[] for i in range(V)]
#flag = 0

def visit(x):
#  if visited[x] == 1:
#    flag = 1
  if not visited[x]:
    visited[x] = 1
    for e in edges[x]:
      visit(e)
    L.append(x)

for i in range(E):
  s, t = map(int,input().split())
  edges[s - 1].append(t - 1)

for i in range(V):
  if not visited[i]:
    visit(i)
L.reverse()

flag = 0
for i in range(V):
  print(L[i] + 1)
  if not flag and i < V - 1 and (L[i + 1] not in edges[L[i]]):
    flag = 1
print(flag)