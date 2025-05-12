import sys
sys.setrecursionlimit(1000000)

WALL = 100
w, h = map(int,input().split())
lst = [[WALL] + list(map(int,input().split())) + [WALL] for i in range(h)]
lst.insert(0, [WALL] * (w + 2))
lst.append([WALL] * (w + 2))

visited = [[0] * (w + 2) for _ in range(h + 2)]
hold = []
app = hold.append

def search(x, y):

  if lst[x][y] == WALL:
    visited[x][y] = 3
    return 3

  if lst[x][y] == 1:
    visited[x][y] = 2
    return 2

  visited[x][y] = 1
  app((x, y))

  if not x % 2:
    pairs = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y)]
  else:
    pairs = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y), (x + 1, y + 1)]
  
  ret = 0
  for t in pairs:
    tx, ty = t[0], t[1]
    v = visited[tx][ty]
    a = 0
    if not v:
      a = search(tx, ty)
    elif v == 3:
      a = 3
    elif v == 2:
      a = 2
    if a > ret:
      ret = a
  return ret

def main():

  for x in range(1, h + 1):
    for y in range(1, w + 1):
      if not visited[x][y] and not lst[x][y]:
        stat = search(x, y)
        for point in hold:
          visited[point[0]][point[1]] = stat
        hold.clear()
  
  ans = 0
  for x in range(1, h + 1):
    for y in range(1, w + 1):
      if lst[x][y]:
        if not x % 2:
          pairs = [(x - 1, y - 1), (x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y)]
        else:
          pairs = [(x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y), (x + 1, y + 1)]
        for t in pairs:
          tx, ty = t[0], t[1]
          if (visited[tx][ty] in [0,3]) and (lst[tx][ty] in [WALL, 0]):
            ans += 1
  
  print(ans)

main()