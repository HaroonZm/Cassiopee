n,k = [int(x) for x in input().split()]
mod = 10**9+7
MAX_N = 10**6
 
fact = [1]
fact_inv = [0]*(MAX_N+4)
for i in range(MAX_N+3):
    fact.append(fact[-1]*(i+1)%mod)

fact_inv[-1] = pow(fact[-1],mod-2,mod)
for i in range(MAX_N+2,-1,-1):
    fact_inv[i] = fact_inv[i+1]*(i+1)%mod
 
 
def mod_comb_k(n,k,mod):
    return fact[n] * fact_inv[k] % mod * fact_inv[n-k] %mod
if k>=n:
  print(mod_comb_k(2*n-1,n,mod))
else:
  res=1
  for i in range(1,k+1):
    res = (res+mod_comb_k(n,i,mod)*mod_comb_k(n-1,n-i-1,mod))%mod
  print(res)