while 1:
  n = int(input())
  if not n:
    break
  tlst = []
  qlst = []
  for _ in range(n):
    m,a,b = map(int,input().split())
    qlst.append((m,a,b))
    tlst += [a,b,b-1]
  tlst = list(set(tlst))
  tlst.sort()
  tdic = {t:i for i,t in enumerate(tlst)}
  lent = len(tlst)
  mp = [0]*lent
  for m,a,b in qlst:
    a,b = tdic[a], tdic[b]
    mp[a] += m
    mp[b] -= m
  acc = 0
  i = 0
  while i < lent:
    acc += mp[i]
    if acc > 150:
      print("NG")
      break
    i += 1
  else:
    print("OK")