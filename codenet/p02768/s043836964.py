N,a,b=map(int,input().split())
mod=10**9+7
n=max(a,b)
fra=[1]*(n+2)
inv=[1]*(n+2)
t=1
for i in range(1,n+2):
    t*=i
    t%=mod
    fra[i]=t
t=pow(fra[n+1],mod-2,mod)
for i in range(n+1,0,-1):
    inv[i]=t
    t*=i
    t%=mod
ans=pow(2,N,mod)-1
tmp=inv[a]
for i in range(1,a+1):
    tmp*=(N+1-i)%mod
    tmp%=mod
ans-=tmp
tmp=inv[b]
for i in range(1,b+1):
    tmp*=((N+1-i)%mod)
    tmp%=mod
ans-=tmp
ans%=mod
print(ans)