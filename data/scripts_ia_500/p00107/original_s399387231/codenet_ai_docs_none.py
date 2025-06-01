def min_diam(A,B,C):
  segments=[A,B,C]
  segments.sort()
  return (segments[0]**2+segments[1]**2)**0.5

while True:
  A,B,C = tuple(map(float,input().split()))
  if (A,B,C) == (0,0,0):
    break
  n = int(input())
  R = [float(input()) for _ in range(n)]
  diam = min_diam(A,B,C)
  for r in R:
    if diam < 2*r:
      print("OK")
    else:
      print("NA")