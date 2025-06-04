n, max_w = map(int, input().split())  # on récupère le nombre d'objets et le poids max

# Bon là je fais mes listes pour les valeurs et poids, j'utilise des 0 au début juste pour simplifier l'indexation, c'est pas ouf mais tant pis
values = [0] * (n + 1)
weights = [0 for _ in range(n + 1)]

for idx in range(1, n+1):
    tmp = input().split()
    values[idx], weights[idx] = int(tmp[0]), int(tmp[1])

# tableau de dp, j'ai toujours du mal à me rappeler l'ordre des dimensions
DP = [[0]*(max_w+1) for _ in range(n+1)]

for i in range(1, n+1):
    for cap in range(1, max_w+1):
        # Bon, là je crois qu'on regarde si ça passe...
        if weights[i] > cap:
            DP[i][cap] = DP[i-1][cap]
        else:
            # Choix : on prend pas l'objet ou bien on essaye deux manières (?) 
            take1 = DP[i][cap-weights[i]] + values[i]
            take2 = DP[i-1][cap-weights[i]] + values[i]
            DP[i][cap] = max(DP[i-1][cap], take1, take2)  #Je mets tout, mais c'est peut-être pas 100% efficace
print(DP[n][max_w])