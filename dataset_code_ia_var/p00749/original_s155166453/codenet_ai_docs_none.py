while True:
  w, h = map(int, input().split())
  if w == 0:
    break
  mp = [[0] + list(input()) + [0] for _ in range(h)]
  mp.insert(0, [0] * (w + 2))
  mp.append([0] * (w + 2))
  for y in range(1, h + 1):
    for x in range(1, w + 1):
      if mp[y][x] == ".":
        mp[y][x] = 0
      else:
        mp[y][x] = int(mp[y][x])
  last_id = 10
  vec = ((0, 1), (0, -1), (1, 0), (-1, 0))
  def update(last_id, target, x, y):
    if mp[y][x] != target:
      return
    mp[y][x] = last_id
    for dx, dy in vec:
      update(last_id, target, x + dx, y + dy)
  for y in range(1, h + 1):
    for x in range(1, w + 1):
      if 1 <= mp[y][x] <= 9:
        update(last_id, mp[y][x], x, y)
        last_id += 1
  node_num = last_id - 10
  edges = [set() for _ in range(node_num)]
  for y in range(1, h + 1):
    for x in range(1, w + 1):
      if mp[y - 1][x] != mp[y][x] and mp[y - 1][x] != 0 and mp[y][x] != 0:
        edges[mp[y][x] - 10].add(mp[y - 1][x] - 10)
  for x in range(1, w + 1):
    if mp[h][x] != 0:
      root = mp[h][x] - 10
      break
  center = [0] * node_num
  ground = [None] * node_num
  for y in range(1, h + 1):
    for x in range(1, w + 1):
      if mp[y][x] != 0:
        target = mp[y][x] - 10
        center[target] += (x + 0.5) / 4
        if mp[y + 1][x] in (0, target + 10):
          continue
        if ground[target] == None:
          ground[target] = [x, x + 1]
        else:
          ground[target][0] = min(ground[target][0], x)
          ground[target][1] = max(ground[target][1], x + 1)
  for x in range(1, w + 1):
    if mp[h][x] == root + 10:
      if ground[root] == None:
        ground[root] = [x, x + 1]
      else:
        ground[root][0] = min(ground[root][0], x)
        ground[root][1] = max(ground[root][1], x + 1)
  total_center = [None] * node_num
  def get_total_center(node):
    mom = center[node]
    wei = 1
    for to in edges[node]:
      to_wei, to_pos = get_total_center(to)
      mom += to_wei * to_pos
      wei += to_wei
    total_center[node] = mom / wei
    return wei, total_center[node]
  get_total_center(root)
  for gr, cen in zip(ground, total_center):
    l, r = gr
    if not (l < cen < r):
      print("UNSTABLE")
      break
  else:
    print("STABLE")