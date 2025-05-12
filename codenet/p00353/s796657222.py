a,b,c = map(int, input().split())
if a >= c:
  print(0)
else:
  d = c - a
  if d <= b:
    print(d)
  else:
    print("NA")