from bisect import bisect_left as bl
INF = 10 ** 20

def main():
  
  w, h = map(int, input().split())
  n = int(input())
  
  xlst = []
  ylst = []
  appx = xlst.append
  appy = ylst.append
  for i in range(n):
    x, y = map(int,input().split())
    appx(x)
    appy(y)
  
  sorted_xlst = sorted(xlst)
  sorted_ylst = sorted(ylst)
  accx = accy = 0
  cum_sum_xlst = []
  cum_sum_ylst = []
  appx = cum_sum_xlst.append
  appy = cum_sum_ylst.append

  for i in range(n):
    accx += sorted_xlst[i]
    accy += sorted_ylst[i]
    appx(accx)
    appy(accy)
  
  if n % 2:
    clx = crx = sorted_xlst[n // 2]
    cly = cry = sorted_ylst[n // 2]
  else:
    clx = sorted_xlst[n // 2 - 1]
    crx = sorted_xlst[n // 2]
    cly = sorted_ylst[n // 2 - 1]
    cry = sorted_ylst[n // 2]
  plx = bl(sorted_xlst, clx)
  prx = bl(sorted_xlst, crx)
  ply = bl(sorted_ylst, cly)
  pry = bl(sorted_ylst, cry)

  xllen = (accx - cum_sum_xlst[plx - 1] * 2 - clx * (n - plx * 2)) * 2 if plx != 0 else (accx - clx * n) * 2
  xrlen = (accx - cum_sum_xlst[prx - 1] * 2 - crx * (n - prx * 2)) * 2 if prx != 0 else (accx - crx * n) * 2
  yllen = (accy - cum_sum_ylst[ply - 1] * 2 - cly * (n - ply * 2)) * 2 if ply != 0 else (accy - cly * n) * 2
  yrlen = (accy - cum_sum_ylst[pry - 1] * 2 - cry * (n - pry * 2)) * 2 if pry != 0 else (accy - cry * n) * 2

  ans = ansx = ansy = INF
  max_sumd = 0
  
  for i in range(n):
    xi = xlst[i]
    yi = ylst[i]

    if xi <= clx:
      cx = crx
      xlen = xrlen
    else:
      cx = clx
      xlen = xllen
    if yi <= cly:
      cy = cry
      ylen = yrlen
    else:
      cy = cly
      ylen = yllen
  
    dx = xi - cx
    if dx < 0:
      dx = -dx

    dy = yi - cy
    if dy < 0:
      dy = -dy

    if max_sumd > dx + dy:
      continue
    else:
      max_sumd = dx + dy
    
    tlen = xlen + ylen - max_sumd

    if ans > tlen:
      ans = tlen
      ansx = cx
      ansy = cy
    elif ans == tlen:
      if ansx > cx:
        ansx = cx
        ansy = cy
      elif ansx == cx:
        if ansy > cy:
          ansy = cy 
  
  print(ans)
  print(ansx, ansy)

main()