from collections import deque
N,M = map(int,input().split())
p = [0] + list(map(int,input().split()))
l = [[] for _ in range(N+1)]
for i in range(M):
  x,y = map(int,input().split())
  l[x].append(y)
  l[y].append(x)

#unionfind
lp = [i for i in range(N+1)] #親のリスト
#木の根を求める
def root(x):
  if lp[x] == x:
    return x
  else:
    lp[x] = root(lp[x])
    return lp[x]
#xとyが同じ集合に属するか否か
def det(x,y):
  return root(x) == root(y)
#xとYが属する集合の併合 Yが親になる
def unite(x,y):
  x = root(x)
  y = root(y)
  if x != y:
    lp[x] = y 

seen = [False]*(N+1)
for i in range(1,N+1):
  if seen[i] == False:
    seen[i] = True
    d = deque([i])
    while len(d)>0:
      v = d.popleft()
      for j in l[v]:
        if seen[j] == False:
          seen[j] = True
          unite(j,i)
          d.append(j)
###
cnt = 0
for i in range(1,N+1):
  cnt += int(det(p[i],i))
print(cnt)