while True:
  n, h = map(int, input().split())
  if n == 0:
    break
  hit = set()
  for _ in range(h):
    c, a, b = input().split()
    if c == "xy":
      add = {(int(a), int(b), z) for z in range(1, n + 1)}
    elif c == "xz":
      add = {(int(a), y, int(b)) for y in range(1, n + 1)}
    elif c == "yz":
      add = {(x, int(a), int(b)) for x in range(1, n + 1)}
    hit = hit | add
  print(n ** 3 - len(hit))