a, b = map(int, input().split())

ans = a+b
if ans < 24:
  print(ans)
else:
  print(ans - 24)