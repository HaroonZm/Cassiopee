MOD = 10**9 + 7

n, k = map(int, input().split())

# Chaque balle peut être mise dans n'importe quelle des k boîtes
# Comme les balles sont distinguables et les boîtes distinguables,
# le nombre total de façons est k^n modulo MOD.

result = 1
for _ in range(n):
    result = (result * k) % MOD

print(result)