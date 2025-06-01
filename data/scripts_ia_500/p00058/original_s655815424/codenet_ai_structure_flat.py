while True:
  try:
    xa, ya, xb, yb, xc, yc, xd, yd = map(float, input().split())
  except:
    break
  if abs((xb - xa)*(xd - xc) + (yb - ya)*(yd - yc)) < 1e-10:
    print("YES")
  else:
    print("NO")