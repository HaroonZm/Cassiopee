from heapq import*
i=input
for _ in'_'*int(i()):
 n,s,x,*y=int(i()),0,[]
 for _ in'_'*n:
  k,l,r=map(int,i().split())
  if l>r:x+=(k,l,r),
  else:y+=(n-k,r,l),
 for x in x,y:
  x.sort();n,*h=len(x),
  while n:
   n-=1
   while x and x[-1][0]>n:k,l,r=x.pop();heappush(h,(r-l,l,r))
   if h:s+=heappop(h)[1]
  for*_,r in x+h:s+=r
 print(s)