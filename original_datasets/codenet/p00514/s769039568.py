def s():
 n,m,r=map(int,input().split())
 r-=n*m
 if r<0:print(0)
 else:
  from math import factorial as f
  print(f(n+r-1)//f(r)//f(n-1))
if'__main__'==__name__:s()