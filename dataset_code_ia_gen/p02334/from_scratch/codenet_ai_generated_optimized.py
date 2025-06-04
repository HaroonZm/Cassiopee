MOD=10**9+7
n,k=map(int,input().split())
max_val=n+k-1
fact=[1]*(max_val+1)
inv_fact=[1]*(max_val+1)
for i in range(2,max_val+1):
    fact[i]=fact[i-1]*i%MOD
inv_fact[max_val]=pow(fact[max_val],MOD-2,MOD)
for i in range(max_val-1,0,-1):
    inv_fact[i]=inv_fact[i+1]*(i+1)%MOD
def comb(a,b):
    if b>a or b<0:
        return 0
    return fact[a]*inv_fact[b]%MOD*inv_fact[a-b]%MOD
print(comb(n+k-1,k-1))