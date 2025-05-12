n, t = map(int, input().split())
min_height = 0
for _ in range(n):
  x, h = map(int, input().split())
  min_height = max(min_height, h / x * t)
print(min_height)