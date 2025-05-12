from heapq import heappush, heappop

def main():
  INF = 10 ** 20
  vec = ((0, 1), (0, -1), (-1, 0), (1, 0))
  
  h, w = map(int, input().split())
  mp = [[-1] + list(map(int, input().split())) + [-1] for _ in range(h)]
  mp.insert(0, [-1] * (w + 2))
  mp.append([-1] * (w + 2))
  
  is_goal = [[False] * (w + 2) for _ in range(h + 2)]
  que = []
  heappush(que, (w, h))
  while que:
    x, y = heappop(que)
    is_goal[y][x] = True
    if mp[y][x] != 0:
        continue
  
    for dx, dy in vec:
      nx, ny =  x + dx, y + dy
      if mp[ny][nx] == -1 or is_goal[ny][nx]:
        continue
      heappush(que, (nx, ny))
  
  costs = [[[INF] * (w + 2) for _ in range(h + 2)] for _ in range(w * h)]
  que = []
  heappush(que, ((0, 0, 1, 1))) #score, dist, x, y
  costs[0][1][1] = 0
  
  while que:
    score, dist, x, y = heappop(que)
    for dx, dy in vec:
      nx, ny = x + dx, y + dy
      
      wood = mp[ny][nx]
      if wood == -1:
        continue
      if dist >= w * h - 1:
        continue
  
      new_score = score + (dist * wood * 2) + wood
      if costs[dist + 1][ny][nx] > new_score:
        costs[dist + 1][ny][nx] = new_score
        heappush(que, (new_score, dist + 1, nx, ny))
  
  ans = min([costs[d][y][x] for y in range(1, h + 1) for x in range(1, w + 1) for d in range(w * h) if is_goal[y][x]])
  print(ans)
  
main()