N,a,b=map(int,input().split())
mod=10**9+7
n=max(a,b)
fra=[1]*(n+2)
inv=[1]*(n+2)
t=1
i=1
while i<n+2:
    t=(t*i)%mod
    fra[i]=t
    i+=1
t=pow(fra[n+1],mod-2,mod)
i=n+1
while i>0:
    inv[i]=t
    t=(t*i)%mod
    i-=1
ans=pow(2,N,mod)-1
tmp=inv[a]
i=1
while i<=a:
    tmp=(tmp*(N+1-i))%mod
    i+=1
ans=(ans-tmp)%mod
tmp=inv[b]
i=1
while i<=b:
    tmp=(tmp*(N+1-i))%mod
    i+=1
ans=(ans-tmp)%mod
print(ans)