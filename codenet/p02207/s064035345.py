from math import log10
from bisect import bisect_left
n=int(input())
l=[[0,0]]+[list(map(int,input().split()))for _ in range(n)]
for i in range(1,n+1):
  l[i][1]=log10(1-l[i][1]/10)
for i in range(n):
  l[i+1][1]+=l[i][1]
q=int(input())
for _ in range(q):
  a,b=map(int,input().split())
  i=bisect_left(l,[a,0])-1
  j=bisect_left(l,[b,0])-1
  p=l[j][1]-l[i][1]+9
  print(10**p)