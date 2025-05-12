from math import gcd

mod=998244353

N=int(input())
a=list(map(int,input().split()))
a.sort()
ans=1
for i in range(N):
    g=gcd(i,a[i])
    ans=(ans*g)%mod

print(ans)