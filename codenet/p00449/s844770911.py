from heapq import*
import sys
r=sys.stdin.readline
def g(n,E,S,G):
 F=[1e7]*-~n;F[S],H=0,[(0,S)]
 while H:
  c,u=heappop(H)
  if u==G:return c
  for f,v in E[u]:
   t=c+f
   if t<F[v]:F[v]=t;heappush(H,(t,v))
 return-1
def s(n,k):
 E=[[]for _ in[0]*-~n]
 for _ in[0]*k:
  f=r();p=map(int,f[2:].split())
  if'0'==f[0]:print(g(n,E,*p))
  else:c,d,e=p;E[c]+=[(e,d)];E[d]+=[(e,c)]
for e in iter(r,'0 0\n'):s(*map(int,e.split()))