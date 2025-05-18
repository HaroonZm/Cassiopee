import sys
from heapq import*
r=sys.stdin.readline
def g(n,E,S,G):
 F=[1e7]*-~n;F[S]=0
 H=[(0,S)]
 while H:
  c,u=heappop(H)
  if u==G:return c
  for f,v in E[u]:
   t=c+f
   if t<F[v]:
    F[v]=t
    heappush(H,(t,v))
 return-1
def s():
 for e in iter(r,'0 0\n'):
  n,k=map(int,e.split())
  E=[[]for _ in[0]*-~n]
  for _ in[0]*k:
   f=r()
   if'0'==f[0]:print(g(n,E,*map(int,f[2:].split())))
   else:
    c,d,e=map(int,f[2:].split())
    E[c]+=[(e,d)];E[d]+=[(e,c)]
s()