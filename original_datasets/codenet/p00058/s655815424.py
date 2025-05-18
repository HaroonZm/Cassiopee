while True:
  try:
    xa, ya, xb, yb, xc, yc, xd, yd = map(float, input().split())
  except:
    break
  abx = xb - xa
  aby = yb - ya
  cdx = xd - xc
  cdy = yd - yc
  if abs(abx * cdx + aby * cdy) < 10**(-10):
    print("YES")
  else:
    print("NO")