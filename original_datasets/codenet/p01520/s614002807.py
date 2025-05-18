n, t, e = map(int, input().split())
xlst = list(map(int, input().split()))
for i, x in enumerate(xlst):
  a = (t - e - 1) // x
  if (a + 1) * x <= t + e:
    print(i + 1)
    break
else:
  print(-1)