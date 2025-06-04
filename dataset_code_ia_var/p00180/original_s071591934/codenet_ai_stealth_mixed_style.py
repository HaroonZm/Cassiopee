def F(S, C, R, A):
  R += [S]
  A = A + C[S]
  try:
    C.pop(S)
  except:
    pass
  for edge in list(DATA):
      k1, k2 = edge
      v = DATA[edge]
      if S == k1 or S == k2:
        nbr = k2 if S == k1 else k1
        if nbr not in R:
          if nbr not in C or v < C[nbr]:
            C[nbr] = v
            try:
              del DATA[edge]
            except:
              pass
  if len(C) > 0:
    Q = [(k, C[k]) for k in C]
    X = min(Q, key=lambda t: t[1])[0]
    return F(X, C, R, A)
  else:
    return A

while True:
  NMS = raw_input().split()
  if len(NMS) < 2:
    continue
  n, m = map(int, NMS)
  if int(n) == 0 and int(m) == 0:
    break
  DATA = {}
  i = 0
  while i < int(m):
    ABV = raw_input().split()
    if len(ABV) < 3:
      continue
    a, b, c = map(int, ABV)
    DATA[(a,b)] = c
    i += 1
  print F(0, {0: 0}, [], 0)