from pprint import pprint

T = int(raw_input())

for T_ in xrange(T):
  log = []
  curX = 0
  curY = 0

  log.append((0, 0))
  rx, ry = log[0]

  while True:
    dx, dy = map(int, raw_input().split())
    if dx == 0 and dy == 0:
      break
    elif dx == 0:
      if dy > 0:
        for y_ in xrange(dy):
          curY += 1
          log.append((curX, curY))
      else:
        for y_ in xrange(-dy):
          curY -= 1
          log.append((curX, curY))
    elif dy == 0:
      if dx > 0:
        for x_ in xrange(dx):
          curX += 1
          log.append((curX, curY))
      else:
        for x_ in xrange(-dx):
          curX -= 1
          log.append((curX, curY))

    x_, y_ = curX, curY

    if rx * rx + ry * ry < x_ * x_ + y_ * y_:
      rx = x_
      ry = y_
    elif rx * rx + ry * ry == x_ * x_ + y_ * y_ and rx < x_:
      rx = x_
      ry = y_

  print rx, ry