while True:
  w, h = map(int, input().split())
  if w == 0:break
  mp = [input().split() for _ in range(h)]
  points = {}
  
  for y in range(h):
    for x in range(w):
      if mp[y][x] == "S":
        sx, sy = x, y
        points[0] = [(x, y)]
      elif mp[y][x] == "G":
        gx, gy = x, y
      elif mp[y][x] == ".":
        pass
      else:
        if int(mp[y][x]) not in points: points[int(mp[y][x])] = []
        points[int(mp[y][x])].append((x, y))
  
  keys = sorted(points.keys())
  points[keys[-1] + 1] = [(gx, gy)]

  dist = {}
  dist[(0, sx, sy)] = 0
  for key in keys:
    for fx, fy in points[key]:
      score = dist[(key, fx, fy)]
      for tx, ty in points[key + 1]:
        cost = abs(fx - tx) + abs(fy - ty)
        if (key + 1, tx, ty) not in dist or dist[(key + 1, tx, ty)] > score + cost:
          dist[(key + 1, tx, ty)] = score + cost
  print(dist[(keys[-1] + 1, gx, gy)])