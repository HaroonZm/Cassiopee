from heapq import heappush, heappop

while True:
  n, m = map(int, input().split())
  if n == 0: break

  mp = ["X" + input() + "X" for _ in range(m)]
  mp.insert(0, "X" * (n + 2))
  mp.append("X" * (n + 2))
  
  que = []
  visited = [[False] * (n + 2) for _ in range(m + 2)]
  sur_flag = False
  for i in range(1, n + 1):
    if mp[1][i] =="&" or mp[m][i] == "&":
      sur_flag = True
      break
    c1, s1 = (1, 0) if mp[1][i] == "#" else (0, 1)
    c2, s2 = (1, 0) if mp[m][i] == "#" else (0, 1)
    heappush(que, (c1, s1, (i, 1)))
    heappush(que, (c2, s2, (i, m)))
    visited[1][i] = True
    visited[m][i] = True
  
  for i in range(1, m + 1):
    if mp[i][1] == "&" or mp[i][n] == "&":
      sur_flag = True
      break
    c1, s1 = (1, 0) if mp[i][1] == "#" else (0, 1)
    c2, s2 = (1, 0) if mp[i][n] == "#" else (0, 1)
    heappush(que, (c1, s1, (1, i)))
    heappush(que, (c2, s2, (n, i)))
    visited[i][1] = True
    visited[i][n] = True
  
  if sur_flag:
    print(0)
    continue
  
  direct = ((0, 1), (0, -1), (1, 0), (-1, 0))
  reached = False
  
  """
  到達コストの低い順で、堀の中にいるものを優先に幅優先探索
  """
  while que and not reached:
    cost, status, point = heappop(que)
    x, y = point
    for dx, dy in direct:
      newx, newy = x + dx, y + dy
      if not visited[newy][newx]:
        visited[newy][newx] = True
        sym = mp[newy][newx]
        if sym == "&":
          print(cost)
          reached = True
          break
        elif sym == "#":
          if status == 1:
            heappush(que, (cost + 1, 0, (newx, newy)))
          else:
            heappush(que, (cost, 0, (newx, newy)))
        elif sym == ".":
          heappush(que,(cost, 1, (newx, newy)))