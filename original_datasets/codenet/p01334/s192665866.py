while True:
  N = int(raw_input())

  if N == 0:
    break

  field = [[(0, 0) for x in xrange(N)] for y in xrange(N)]

  for y in xrange(N):
    line = map(int, raw_input().split())

    for x in xrange(N):
      field[y][x] = (line[2 * x + 1], line[2 * x])

  vis = set()

  cnt = 0

  for y in xrange(N):
    for x in xrange(N):

      cur = (y, x)

      if cur in vis: continue

      loop = set()
      loop.add(cur)

      while True:
        cur = field[cur[0]][cur[1]]

        if cur in vis:
          loop.add(cur)
          vis = vis | loop
          break

        if cur in loop:
          loop.add(cur)
          cnt += 1
          vis = vis | loop
          break

        loop.add(cur)
  print cnt