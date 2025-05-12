while True:
  b = int(input())
  if b == 0:break
  x = b * 2
  for k in range(int(x ** (1 / 2)), 0, -1):
    if x % k == 0:
      if (-k + 1 + (x // k)) % 2 == 0:
        a = (-k + 1 + x // k) // 2
        if a > 0:
          print(a, k)
          break