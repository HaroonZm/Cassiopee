from collections import defaultdict

mod = 10**9+7
rng = 200100
fctr = [1]
finv = [1]
for i in range(1,rng):
  fctr.append(fctr[-1]*i%mod)
for i in range(1,rng):
  finv.append(pow(fctr[i],mod-2,mod))
def cmb(n,k):
  if n<0 or k<0:
    return 0
  else:
    return fctr[n]*finv[n-k]*finv[k]%mod

import sys
input = sys.stdin.readline
n,X,Y = map(int,input().split())
cw = [list(map(int,input().split())) for i in range(n)]
cw.sort()
mnls = []
graph = [[] for i in range(n)]
notmn = set()
for i in range(n):
  if i == 0 or cw[i-1][0] != cw[i][0]:
    mnls.append((i,cw[i][0],cw[i][1]))
  else:
    if cw[i][1]+mnls[-1][2] <= X:
      graph[i].append(mnls[-1][0])
      graph[mnls[-1][0]].append(i)
    else:
      notmn.add(i)
mnls.sort(key = lambda x:x[2])
for i,x in enumerate(mnls):
  if i == 0:
    continue
  if x[2]+mnls[0][2] <= Y:
    graph[x[0]].append(mnls[0][0])
    graph[mnls[0][0]].append(x[0])
for i in notmn:
  if mnls[0][1] != cw[i][0]:
    if mnls[0][2]+cw[i][1] <= Y:
      graph[i].append(mnls[0][0])
      graph[mnls[0][0]].append(i)
  else:
    if len(mnls) >= 2 and mnls[1][2]+cw[i][1] <= Y:
      graph[i].append(mnls[1][0])
      graph[mnls[1][0]].append(i)
vis = [0 for i in range(n)]
ans = 1
for i in range(n):
  if vis[i]:
    continue
  vis[i] = 1
  stack = [i]
  color = defaultdict(int)
  while stack:
    x = stack.pop()
    color[cw[x][0]] += 1
    for y in graph[x]:
      if vis[y] == 0:
        vis[y] = 1
        stack.append(y)
  sm = sum(color.values())
  for v in color.values():
    ans = ans*cmb(sm,v)%mod
    sm -= v
print(ans)