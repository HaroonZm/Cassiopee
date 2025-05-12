import sys
input = sys.stdin.readline
import math

N=int(input())
ans=[0]*(N+1)
sn=int(math.sqrt(N)+1)
for x in range(1,sn+1):
  for y in range(1,sn+1):
    for z in range(1,sn+1):
      i=x**2+y**2+z**2+x*y+y*z+z*x
      if 1<=i<=N:
        ans[i]+=1
for h in range(1,N+1):          
  print(ans[h])