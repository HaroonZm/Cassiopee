from bisect import *

n=int(input())
a=sorted(list(map(int,input().split())))
N=a[-1]
inx=bisect(a,N//2)
a=[a[0]]+a+[a[-1]]
th=10**9
for i in [a[inx-1],a[inx],a[inx+1]]:
 if abs(i-N//2)<=th and i<N:
  R=i
  th=abs(i-N//2)
print(N,R)