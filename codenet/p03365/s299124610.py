n=int(input())
mod=10**9+7
fra=[1]*(n+2)
inv=[1]*(n+2)
t1=1
t2=1
for i in range(1,n+2):
    t1*=i
    t1%=mod
    t2*=pow(i,mod-2,mod)
    t2%=mod
    fra[i]=t1
    inv[i]=t2
ans=fra[n]
for i in range((n+1)//2,n):
    ans-=fra[i-1]*inv[2*i-n]*fra[i]%mod
    ans%=mod
print(ans)