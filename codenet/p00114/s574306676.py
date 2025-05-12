def f(a,b):
  p,q=a,b
  while q!=0: p,q=q,p%q
  return a/p*b
  
while 1:
  x=map(int,raw_input().split())
  if any(x)==0: break
  A=[]
  for i in range(0,6,2):
    a,b=x[i:i+2]
    c=1
    for j in range(1,b):
      c=(c*a)%b
      if c==1: break
    A.append(j)
  a,b,c=A
  print f(f(a,b),c)