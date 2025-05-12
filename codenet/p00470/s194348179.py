while True:
  h,w = map(int, input().split())
  if not h:
    break
#dp[R][U][""]
  h -= 1
  w -= 1
  mp = {(0,2,"UU") : 1, (2,0,"RR") : 1, (1,1,"UR") : 1, (1,1,"RU") : 1}
  for i in range(h + 1):
    for j in range(w + 1):
      if i + j <= 2:
        continue
      mp[(i, j, 'UU')] = 0
      if (i, j - 1, 'UU') in mp:
        mp[(i, j, 'UU')] += mp[(i, j - 1, 'UU')]
      if (i, j - 1, 'RU') in mp:
        mp[(i, j, 'UU')] += mp[(i, j - 1, 'RU')]
      mp[(i, j, 'RR')] = 0
      if (i - 1, j, 'RR') in mp:
        mp[(i, j, 'RR')] += mp[(i - 1, j, 'RR')]
      if (i - 1, j, 'UR') in mp:
        mp[(i, j, 'RR')] += mp[(i - 1, j, 'UR')]
      mp[(i, j, 'UR')] = 0
      if (i - 1, j, 'UU') in mp:
        mp[(i, j, 'UR')] += mp[(i - 1, j, 'UU')]
      mp[(i, j, 'RU')] = 0
      if (i, j - 1, 'RR') in mp:
        mp[(i, j, 'RU')] += mp[(i, j - 1, 'RR')]
  print((mp[(h, w, 'UU')] + mp[(h, w, 'UR')] + mp[(h, w, 'RU')] + mp[(h, w, 'RR')]) % 100000)