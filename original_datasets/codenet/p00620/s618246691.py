while True:
  n = int(input())
  if n == 0:break
  mp = [list(map(int, input().split())) for _ in range(n)]
  used = [[False] * n for _ in range(n)]
  
  inits = []
  for y in range(n):
    for x in range(n):
      if mp[y][x] < 0:
        inits.append((x, y, mp[y][x]))
        used[y][x] = True
  
  vec = ((0, 1), (-1, 0), (0, -1), (1, 0))
  
  def search(x, y, s, index, inits, end):
    if s == 0 and index == end:
      return True
    elif s == 0:
      x, y, s = inits[index]
      index += 1
    
    ret = False
    for dx, dy in vec:
      nx, ny = x + dx, y + dy
      if 0 <= nx < n and 0 <= ny < n and not used[ny][nx] and mp[ny][nx] + s <= 0:
        used[ny][nx] = True
        ret = ret or search(nx, ny, s + mp[ny][nx], index, inits, end)
        used[ny][nx] = False
    return ret
  
  if sum([sum(lst) for lst in mp]) != 0:
    print("NO")
  else:
    if search(0, 0, 0, 0, inits, len(inits)):
      print("YES")
    else:
      print("NO")