from collections import deque, defaultdict
n, m, s, t = map(int, input().split())
s -= 1
t -= 1
edges = [[] for _ in range(n)]
for _ in range(m):
  x, y = map(int, input().split())
  x -= 1
  y -= 1
  edges[x].append(y)
  edges[y].append(x)

def dist_from(s):
  INF = 10 ** 20
  dist = [INF] * n
  dist[s] = 0
  que = deque()
  que.append((0, s))
  while que:
    score, node = que.popleft()
    for to in edges[node]:
      if dist[to] > score + 1:
        dist[to] = score + 1
        que.append((score + 1, to))
  return dist

dist_from_s = dist_from(s)
dic1 = {}
for i, d in enumerate(dist_from_s):
  if d in dic1:
    dic1[d].add(i)
  else:
    dic1[d] = {i}

dist_from_t = dist_from(t)
dic2 = {}
for i, d in enumerate(dist_from_t):
  if d in dic2:
    dic2[d].add(i)
  else:
    dic2[d] = {i}

st_dist = dist_from_s[t]
ans = 0
for key in dic1:
  another_key = st_dist - key - 2
  if another_key in dic2:
    add = len(dic1[key]) * len(dic2[another_key])
    for u in dic1[key]:
      for to in edges[u]:
        if to in dic2[another_key]:
          add -= 1
    ans += add
print(ans)