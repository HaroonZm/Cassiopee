from fractions import Fraction as F
from operator import itemgetter as ig
def MAIN():
  n,c=[int(x) for x in input().split()]
  x=[]
  append=x.append
  for _ in range(n):
    v,w=[int(z) for z in input().split()]
    append( (F(v,w), v, w) )
  x.sort(key=ig(0),reverse=1)
  t=0
  while x:
    ratio,vv,ww=x.pop(0)
    if c>ww-1:
      c-=ww
      t+=vv
    else:
      t+=ratio*c
      c=0
      break
  print(float(t) if not t.denominator-1 else int(t))
MAIN()