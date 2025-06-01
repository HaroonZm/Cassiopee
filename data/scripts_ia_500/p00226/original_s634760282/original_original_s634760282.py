while True:
  r, a = input().split()
  if r == "0":
    break
  
  hit = 0
  for x, y in zip(r, a):
    if x == y:
      hit += 1
  
  blow = -hit
  for x in r:
    if x in a:
      blow += 1

  print(hit, blow)