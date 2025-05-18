n, m = map(int, input().split())
if n % 2:
  print(*[0] * (n // 2) + [m] * (n // 2 + 1))
else:
  print(*[0] * (n // 2 - 1) + [m] * (n // 2 + 1))