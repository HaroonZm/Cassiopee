t = int(input())
for i in range(t):
  h, w = map(int, input().split())
  mp = [list("#" + input() + "#") for _ in range(h)]
  mp.insert(0, ["#"] * (w + 2))
  mp.append(["#"] * (w + 2))
  for y in range(h + 2):
    for x in range(w + 2):
      if mp[y][x] == ">":
        sx, sy, sd = x, y, 0
      if mp[y][x] == "^":
        sx, sy, sd = x, y, 1
      if mp[y][x] == "<":
        sx, sy, sd = x, y, 2
      if mp[y][x] == "v":
        sx, sy, sd = x, y, 3
  mp[sy][sx] = "."
  n = int(input())
  s = input()
  vec = ((1, 0), (0, -1), (-1, 0), (0, 1))
  dic = {"R":0, "U":1, "L":2, "D":3}
  tank = {0:">", 1:"^", 2:"<", 3:"v"}
  for c in s:
    if c == "S":
      dx, dy = vec[sd]
      nx, ny = sx, sy
      while mp[ny][nx] not in ("#", "*"):
        nx += dx
        ny += dy
      if mp[ny][nx] == "*":
        mp[ny][nx] = "."

    else:
      sd = dic[c]
      dx, dy = vec[sd]
      if mp[sy + dy][sx + dx] == ".":
        sx += dx
        sy += dy

  mp[sy][sx] = tank[sd]
  for j in range(1, h + 1):
    print("".join(mp[j][1:-1]))
  if i != t - 1:
    print()