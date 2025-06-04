from heapq import heappush, heappop

def main():
  INF = 10 ** 7
  h, w = map(int, input().split())
  mp = [[INF] + list(map(int, input().split())) + [INF] for _ in range(h)]
  mp.insert(0, [INF] * (w + 2))
  mp.append([INF] * (w + 2))
  ridge = [[None] * (w + 2) for _ in range(h + 2)]
  vec = ((1, 0), (0, -1), (-1, 0), (0, 1))
  
  def is_ridge(x, y):
    to_set = set()
    for dx, dy in vec:
      nx, ny = x + dx, y + dy
      temp = ridge[ny][nx]
      if temp != None:
        if temp is True:
          ridge[y][x] = True
          return True
        else:
          to_set.add(temp)
    if not to_set:
      ridge[y][x] = (x, y)
    elif len(to_set) == 1:
      ridge[y][x] = list(to_set)[0]
    else:
      ridge[y][x] = True
    return ridge[y][x]
  
  que = []
  for y in range(1, h + 1):
    for x in range(1, w + 1):
      h = mp[y][x]
      heappush(que, (h, x, y))
  
  ans = 0
  while que:
    _, x, y = heappop(que)
    if is_ridge(x, y) is True:
      ans += 1
  print(ans)

main()