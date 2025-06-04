mod = 10**9+7
n,k=map(int,input().split())
if n>k:
    print(0)
    exit()
fact=[1]*(k+1)
for i in range(1,k+1):
    fact[i]=fact[i-1]*i%mod
inv=[1]*(k+1)
inv[k]=pow(fact[k],mod-2,mod)
for i in range(k-1,0,-1):
    inv[i]=(inv[i+1]*(i+1))%mod
def perm(n,r):
    return fact[n]*inv[n-r]%mod
print(perm(k,n))