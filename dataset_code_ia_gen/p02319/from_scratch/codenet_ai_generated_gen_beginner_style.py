N, W = map(int, input().split())
items = []
for _ in range(N):
    v, w = map(int, input().split())
    items.append((v, w))

max_value = 0
# Comme poids et capacité sont très grands, on utilise la solution par valeur
# Calcul de la somme max des valeurs
sum_values = sum(v for v, w in items)

# dp[val] = poids minimum pour atteindre exactement la valeur val
dp = [10**15] * (sum_values + 1)
dp[0] = 0

for v, w in items:
    for val in range(sum_values - v, -1, -1):
        if dp[val] + w <= W:
            if dp[val + v] > dp[val] + w:
                dp[val + v] = dp[val] + w

for val in range(sum_values, -1, -1):
    if dp[val] <= W:
        print(val)
        break