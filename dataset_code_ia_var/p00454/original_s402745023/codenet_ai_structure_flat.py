while True:
  w, h = map(int, input().split())
  if not w:
    break

  n = int(input())

  xlst = [0, w - 1]
  ylst = [0, h - 1]
  plst = []

  for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    plst.append([x1, y1, x2 - 1, y2 - 1])
    xlst.append(x1)
    xlst.append(x2)
    xlst.append(x2 - 1)
    ylst.append(y1)
    ylst.append(y2)
    ylst.append(y2 - 1)

  xlst = list(set(xlst))
  ylst = list(set(ylst))
  xlst.sort()
  ylst.sort()

  xdic = {}
  ydic = {}
  idx = 0
  for v in xlst:
    xdic[v] = idx
    idx += 1
  idx = 0
  for v in ylst:
    ydic[v] = idx
    idx += 1

  neww = xdic[xlst[-1]]
  newh = ydic[ylst[-1]]

  painted = [[1] * (newh + 2)]
  for _ in range(neww):
    painted.append([1] + [0] * newh + [1])
  painted.append([1] * (newh + 2))

  for p in plst:
    x1, y1, x2, y2 = p
    x1 = xdic[x1] + 1
    y1 = ydic[y1] + 1
    x2 = xdic[x2] + 1
    y2 = ydic[y2] + 1
    for x in range(x1, x2 + 1):
      for y in range(y1, y2 + 1):
        painted[x][y] = 1

  stack = []
  app = stack.append
  pp = stack.pop
  dx1 = -1
  dx2 = 1
  dy1 = 0
  dy2 = 0
  dx3 = 0
  dx4 = 0
  dy3 = -1
  dy4 = 1
  ans = 0

  x = 1
  while x <= neww:
    y = 1
    while y <= newh:
      if not painted[x][y]:
        ans += 1
        painted[x][y] = 1
        app((x, y))
        while stack:
          px, py = pp()
          tx = px + dx1
          ty = py + dy1
          if not painted[tx][ty]:
            painted[tx][ty] = 1
            app((tx, ty))
          tx = px + dx2
          ty = py + dy2
          if not painted[tx][ty]:
            painted[tx][ty] = 1
            app((tx, ty))
          tx = px + dx3
          ty = py + dy3
          if not painted[tx][ty]:
            painted[tx][ty] = 1
            app((tx, ty))
          tx = px + dx4
          ty = py + dy4
          if not painted[tx][ty]:
            painted[tx][ty] = 1
            app((tx, ty))
      y += 1
    x += 1
  print(ans)