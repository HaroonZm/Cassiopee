while True:
  r, c, q = map(int, input().split())
  if r == 0: break
  querys = [list(map(int, input().split())) for _ in range(q)]
  querys.reverse()
  r_used = [False] * r
  c_used = [False] * c
  r_cnt = c
  c_cnt = r
  ans = 0
  for a, b, o in querys:
    if a == 0:
      if not r_used[b]:
        r_used[b] = True
        c_cnt -= 1
        if o:
          ans += r_cnt

    else:
      if not c_used[b]:
        c_used[b] = True
        r_cnt -= 1
        if o:
          ans += c_cnt
  print(ans)