mp = [list("X" * 10)] + [list("X" + input() + "X") for _ in range(8)] + [list("X" * 10)]
vec = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))
#mami...o, witch...x

def search(target, another, x, y, dx, dy):
  nx, ny = x + dx, y + dy
  cnt = 0
  while mp[ny][nx] == another:
    nx += dx
    ny += dy
    cnt += 1

  if mp[ny][nx] == target:
    return cnt
  else:
    return 0

def score(target, another, x, y):
  ret = 0
  for dx, dy in vec:
    ret += search(target, another, x, y, dx, dy)
  return ret

def locate(target, another, x, y):
  mp[y][x] = target
  for dx, dy in vec:
    if search(target, another, x, y, dx, dy):
      nx, ny = x + dx, y + dy
      while mp[ny][nx] == another:
        mp[ny][nx] = target
        nx += dx
        ny += dy

def temp(target, another, flag):
  max_score = 0
  max_x, max_y = 100, 100
  loop = range(1, 9) if flag else range(8, 0, -1)
  for y in loop:
    for x in loop:
      if mp[y][x] != ".":continue
      new_score = score(target, another, x, y)
      if new_score > max_score:
        max_score = new_score
        max_x, max_y = x, y
  
  if max_score != 0:
    locate(target, another, max_x, max_y)
    return True
  return False

def mami():
  return temp("o", "x", True)

def witch():
  return temp("x", "o", False)

def play():
  while True:
    flag = False
    flag = mami() or flag
    flag = witch() or flag
    if not flag:break
play()
[print("".join(lst[1:-1])) for lst in mp[1:-1]]