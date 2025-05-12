while True:
  ns = list(map(int, input().split()))
  if not any(ns):
    break
  a = ns[0] + ns[3]
  b = ns[1] + ns[4]
  c = ns[2] + ns[5]
  av, ar = a // 3, a % 3
  bv, br = b // 3, b % 3
  cv, cr = c // 3, c % 3
  if max(ar, br, cr) == 0:
    print(av + bv + cv)
  elif max(ar, br, cr) == 1:
    print(av + bv + cv + min(ar, br, cr))
  elif max(ar, br, cr) == 2:
    if [ar, br, cr].count(2) == 3:
      print(av + bv + cv + 2)
    elif [ar, br, cr].count(2) == 2:
      for xr, xv in ((ar, av), (br, bv), (cr, cv)):
        if xr == 2:
          continue
        if xv == 0:
          print(av + bv + cv + xr)
        else:
          print(av + bv + cv + 1)
        break
    else:
      print(av + bv + cv + min(ar, br, cr))