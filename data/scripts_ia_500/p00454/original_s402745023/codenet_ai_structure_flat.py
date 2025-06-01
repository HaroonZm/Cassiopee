while True:
  w, h = map(int, input().split())
  if w == 0:
    break
  n = int(input())
  xlst = [0, w - 1]
  ylst = [0, h - 1]
  plst = []
  for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    plst.append([x1, y1, x2 - 1, y2 - 1])
    xlst += [x1, x2, x2 - 1]
    ylst += [y1, y2, y2 - 1]
  xlst = sorted(set(xlst))
  ylst = sorted(set(ylst))
  xdic = {}
  ydic = {}
  for i, v in enumerate(xlst):
    xdic[v] = i
  for i, v in enumerate(ylst):
    ydic[v] = i
  neww = xdic[xlst[-1]]
  newh = ydic[ylst[-1]]
  painted = [[1]*(newh+2)]
  for _ in range(neww):
    painted.append([1]+[0]*newh+[1])
  painted.append([1]*(newh+2))
  for p in plst:
    x1, y1, x2, y2 = p
    x1 = xdic[x1]+1
    y1 = ydic[y1]+1
    x2 = xdic[x2]+1
    y2 = ydic[y2]+1
    for x in range(x1, x2+1):
      for y in range(y1, y2+1):
        painted[x][y] = 1
  stack = []
  ans = 0
  for x in range(1, neww+1):
    for y in range(1, newh+1):
      if painted[x][y] == 0:
        ans += 1
        painted[x][y] = 1
        stack.append((x,y))
        while stack:
          px, py = stack.pop()
          for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            tx, ty = px+dx, py+dy
            if painted[tx][ty] == 0:
              painted[tx][ty] = 1
              stack.append((tx,ty))
  print(ans)