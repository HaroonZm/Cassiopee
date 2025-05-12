def read():
  return list(map(int,input().split()))

while 1:
  try:
    n,w,h=read()
    bases=[(0,0,0)]*n
    for i in range(n):
      bases[i]=read()
  except: break
  
  res1=True
  ls,rs=zip(*sorted([(x-w,x+w) for x,y,w in bases],key=lambda lr:lr[0]))
  x=0
  for l,r in zip(ls,rs):
    res1&=l<=x
    x=max(x,r)
  res1&=w<=x
  
  res2=True
  ls,rs=zip(*sorted([(y-w,y+w) for x,y,w in bases],key=lambda lr:lr[0]))
  x=0
  for l,r in zip(ls,rs):
    res2&=l<=x
    x=max(x,r)
  res2&=h<=x
  
  print("Yes" if res1 or res2 else "No")