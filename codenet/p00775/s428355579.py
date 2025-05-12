import math

while True:
  (r, n) = map(int, raw_input().split())
  if r + n == 0: break

  hs = {}
  for i in range(-22, 22 + 1):
    hs[i] = 0

  for _ in range(n):
    (xl, xr, h) = map(int, raw_input().split())
    for i in range(xl, xr):
      hs[i] = max(hs[i], h)

  ans = 10 ** 9
  for i in range(-r, r):
    p = i
    if i < 0: p += 1
    rr = hs[i] + r - math.sqrt(r * r - p * p)
    ans = min(ans, rr)

  print "%.10f" % max(0, ans)