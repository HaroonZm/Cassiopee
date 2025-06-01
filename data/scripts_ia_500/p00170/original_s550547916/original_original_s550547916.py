def solve(placed, w1, w2):
  n = len(N) - len(placed)
  x = list(set(N) - set(placed))
  if x == []:
    a = tuple(placed)
    D1[a] = w1
    D2[a] = w2
    return
  
  for e in x:
    w = Food[e][0]
    if w2 > Food[e][1]: return
    a = w1 + w * n
    b = w2 + w
    solve(placed+[e], a, b)
  return

while 1:
  n = input()
  if n==0: break
  D1 = {}
  D2 = {}
  Name = {}
  Food = {}
  N = range(n)
  for i in N:
    a = raw_input().split()
    Food[i] = map(int, a[1:])
    Name[i] = a[0]
    
  solve([], 0, 0)
  
  Index, e = sorted(D1.items(), key = lambda x: x[1])[0]
  for e in list(Index)[::-1]:
    print Name[e]