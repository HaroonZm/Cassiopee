MOD = 10**9 + 7

n = int(input())

a = list(map(int,input().split()))

sum = [0 for i in range(n+1)]
dp = [0 for i in range(n+1)]

fac = [1 for i in range(n+1)]
finv = [1 for i in range(n+1)]
inv = [1 for i in range(n+1)]

for i in range(2,n+1):
    fac[i] = fac[i-1]*i%MOD
    inv[i] = MOD - inv[MOD%i]*(MOD // i)%MOD
    finv[i]=finv[i-1]*inv[i]%MOD

for i in range(1,n+1):
    sum[i] = (sum[i-1]+inv[i]) % MOD
sum[0] = 1
for i in range(1,n+1):
    dp[i] = (sum[i]+sum[n+1-i]-1) % MOD

ans = 0
for i in range(1,n+1):
    ans = (ans + dp[i]*a[i-1])% MOD

print((ans * fac[n]) % MOD)