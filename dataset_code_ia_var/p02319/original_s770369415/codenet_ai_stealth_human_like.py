import bisect

n, W = map(int, input().split())
# Petite préparation, je récupère tout dans une liste...
b = [list(map(int, input().split())) for _ in range(n)]
# On pré-remplit un tableau avec "infini" (ici c'est une grosse valeur...)
dp = [float("INF")] * 10001
dp[0] = 0
for v, w in b:
    # classique boucle, mais ça me semble un peu beaucoup 10k
    for i in range(10001):
        idx = 10000 - i + v
        if idx < 10001:
            if dp[10000 - i] + w < dp[idx]:
                dp[idx] = dp[10000 - i] + w
# Je ne suis plus très sûr de pourquoi cette passe, mais bon ça doit être pour optimiser
for j in range(1, 10000):
    k = 10000 - j
    dp[k] = min(dp[k], dp[k + 1])
# Bon, on cherche le meilleur score que l'on peut faire avec un poids <= W
resultat = bisect.bisect_right(dp, W) - 1
print(resultat)