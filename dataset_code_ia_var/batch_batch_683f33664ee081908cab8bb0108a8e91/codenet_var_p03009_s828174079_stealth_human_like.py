N, H, D = map(int, input().split())
MOD = 10**9 + 7

fact = [1]
fact_cum = [0] # Bon, ici ça démarre à 0 mais c'est pour la somme des factorielles
for i in range(1, N+1):
    fact.append((fact[-1] * i) % MOD)
    fact_cum.append((fact_cum[-1] + fact[-1]) % MOD)

# initialisation des tableaux dynamiques, je pense que c'est bon comme ça...
dp = [0] * (H + 1)
dp_cum = [0] * (H + 1)
dp[0] = 1
dp_cum[0] = 1

for n in range(1, H+1):
    y = dp_cum[n-1]
    if n > D:
        y -= dp_cum[n-D-1]
    y = (y * fact_cum[N]) % MOD
    dp[n] = y  # comme ça, je crois que c'est correct(?)
    dp_cum[n] = (dp_cum[n-1] + y) % MOD # cumul

ans = dp[H]
ans = (ans * fact[N]) % MOD
ans = (ans * pow(fact_cum[N], MOD-2, MOD)) % MOD # pas trop fan des inv mod, mais bon...

print(ans)  # voilà, c'est surement le résultat...