m, n = map(int, input().split())
mp = [list("#" * (n + 2))] + [list("#" + input() + "#") for _ in range(m)] + [list("#" * (n + 2))]
vec = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1))
for y in range(1, m + 1):
  for x in range(1, n + 1):
    if mp[y][x] == "x":
      for dx, dy in vec:
        if mp[y + dy][x + dx] == "-":
          mp[y + dy][x + dx] = "#"
    if mp[y][x] == "o":
      if mp[y][x - 1] == "-":mp[y][x - 1] = "#"
      if mp[y][x + 1] == "-":mp[y][x + 1] = "#"
for x in range(1, n + 1):
  if mp[1][x] == "-": mp[1][x] = "#"

print(sum([line.count("-") for line in mp]))