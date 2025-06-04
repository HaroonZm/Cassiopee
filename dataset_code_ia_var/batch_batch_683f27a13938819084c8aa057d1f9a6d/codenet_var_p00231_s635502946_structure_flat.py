while True:
  n = int(input())
  if n == 0:
    break
  tlst = []
  qlst = []
  for _ in range(n):
    m, a, b = map(int, input().split())
    qlst.append((m, a, b))
    tlst.append(a)
    tlst.append(b)
    tlst.append(b - 1)
  tlst = list(set(tlst))
  tlst.sort()
  tdic = {}
  for i in range(len(tlst)):
    tdic[tlst[i]] = i
  lent = len(tlst)
  mp = []
  for _ in range(lent):
    mp.append(0)
  for q in qlst:
    m, a, b = q
    a = tdic[a]
    b = tdic[b]
    mp[a] += m
    mp[b] -= m
  acc = 0
  ok = True
  for i in range(lent):
    acc += mp[i]
    if acc > 150:
      print("NG")
      ok = False
      break
  if ok:
    print("OK")