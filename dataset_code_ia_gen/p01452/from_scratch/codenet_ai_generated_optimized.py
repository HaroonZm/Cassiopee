MOD=10**9+7
MAX=200000
fact=[1]*(MAX+1)
inv=[1]*(MAX+1)
inv_fact=[1]*(MAX+1)
for i in range(2,MAX+1):
    fact[i]=fact[i-1]*i%MOD
    inv[i]=MOD - (MOD//i)*inv[MOD%i]%MOD
for i in range(2,MAX+1):
    inv_fact[i]=inv_fact[i-1]*inv[i]%MOD
def comb(n,r):
    if r<0 or r>n:
        return 0
    return fact[n]*inv_fact[r]%MOD*inv_fact[n-r]%MOD
N,M,K=map(int,input().split())
res=comb(N+M+2*K,N+K)
print(res%MOD)