from collections import deque
h, w, s, t = input().split()
h, w = int(h), int(w)
mp = ["#" * (w + 2)] + ["#" + input() + "#" for _ in range(h)] + ["#" * (w + 2)]
checked = [[False] * (w + 2) for _ in range(h + 2)]
edges = {chr(c):[] for c in range(ord("A"), ord("Z") + 1)}
for y in range(1, h + 1):
  for x in range(1, w + 1):
    if mp[y][x] == "|" and not checked[y][x]:
      nx, ny = x, y
      start = mp[ny - 2][nx]
      while mp[ny][nx] == "|":
        checked[ny][nx] = True
        ny += 1
      goal = mp[ny + 1][nx]
      edges[start].append(goal)
      edges[goal].append(start)
    
    if mp[y][x] == "-" and not checked[y][x]:
      nx, ny = x, y
      start = mp[ny][nx - 2]
      while mp[ny][nx] == "-":
        checked[ny][nx] = True
        nx += 1
      goal = mp[ny][nx + 1]
      edges[start].append(goal)
      edges[goal].append(start)

que = deque()
que.append((0, s))
used = {}
used[s] = True
while que:
  cost, node = que.popleft()
  if node == t:
    print(cost)
    break
  for to in edges[node]:
    if not to in used:
      used[to] = True
      que.append((cost + 1, to))