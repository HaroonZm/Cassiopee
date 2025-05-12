N, H, D = map(int,input().split())
MOD = 10**9 + 7

fact = [1]
fact_cum = [0] # 1! to N!
for i in range(1,N+1):
  fact.append((fact[-1]*i)%MOD)
  fact_cum.append((fact_cum[-1] + fact[-1])%MOD)

dp = [0] * (H+1)
dp_cum = [0] * (H+1)
dp[0] = 1
dp_cum[0] = 1

for n in range(1,H+1):
  x = dp_cum[n-1]
  if n > D:
    x -= dp_cum[n-D-1]
  x *= fact_cum[N]
  x %= MOD
  dp[n] = x
  dp_cum[n] = (dp_cum[n-1] + x)%MOD

answer = dp[H]
answer *= fact[N]
answer %= MOD
answer *= pow(fact_cum[N],MOD-2,MOD)
answer %= MOD

print(answer)