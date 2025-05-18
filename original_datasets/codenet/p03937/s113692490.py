h, w = map(int, input().split())

ans = 0
for i in range(h):
  ans += input().count("#")

print("Possible" if h + w - 1 == ans else "Impossible")