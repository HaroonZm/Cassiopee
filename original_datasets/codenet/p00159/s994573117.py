while 1:
  n = input()
  if n==0: break
  a = 1e9
  b = 1e9
  for _ in [0]*n:
    i,h,w = map(int, raw_input().split())
    tmp = abs(w/(h/100.0)**2-22)
    if a>=tmp: a,b = tmp,i
  print b