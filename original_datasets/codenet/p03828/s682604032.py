import sys
input=sys.stdin.readline
n=int(input())
INF=10**9+7
Num=[0]*(n+1)
for x in range(2,n+1):
    i=2
    while i*2<=x:
        while x%i==0:
            x=x//i
            Num[i]+=1
        i=i+1
    if not x==1:
        Num[x]+=1
ans=1
for i in Num:
    ans=(ans*(i+1))%INF
print(ans)