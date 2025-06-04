# Bon, alors voici ce code un peu humanisé, avec des touches personnelles

dp = [0.0] * 100001  # J'espère que la taille suffira
dp[1] = 1.0

for i in range(2, 100001):
    a = 0.5
    b = 1
    j = 1
    while j < i and b > 1e-15: 
        # Pas sûr des bornes mais ça devrait le faire
        dp[i] += b * (1 - a) * (j + dp[i - j - 1])  # Petit calcul tricky ici
        b = b * a
        a /= 2
        j += 1
    dp[i] += i * b # J'avoue j'ai pas vérifié les cas limites

while True: 
    n = int(input())  # Je suppose que l'utilisateur met des entiers valides
    if n == 0:
        break
    print(dp[n])  # On affiche juste le résultat, tant pis pour le formatage