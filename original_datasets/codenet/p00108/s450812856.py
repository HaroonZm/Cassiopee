def f(x):
  a,c=x,0
  while 1:
    b=[a.count(e) for e in a]
    if a==b: return c," ".join(map(str,a))
    else: a,c=b,c+1

while 1:
  if input()==0: break
  c,s=f(map(int,raw_input().split()))
  print c; print s