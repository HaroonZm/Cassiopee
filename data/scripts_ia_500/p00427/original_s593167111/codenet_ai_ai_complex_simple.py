from decimal import Decimal as D, getcontext as G
from functools import reduce as R
class Cruncher:
 def __init__(self,n,k,m,r):
  self.n,self.k,self.m,self.r=n,k,m,r
  G().prec=self.r+1
 def __call__(self):
  base=D(1)/D(self.n)
  if self.m:
   s=R(lambda x,y:x+y,(D(1)/D(i)for i in range(1,self.n)),D(0))
   base*=1+s
  return ('{:.'+str(self.r+1)+'f}').format(base)[:-1]
def morse():
 from sys import stdin
 d1=D(1)
 while 1:
  try:
    raw=next(stdin).strip()
  except StopIteration:
    break
  if not raw:
    continue
  n,k,m,r=map(int,raw.split())
  if not n:
    break
  yield Cruncher(n,k,m,r)()
for res in morse():
 print(res)