n = int(input())
vals = list(map(int, input().split()))
dp = [[0, 0, 0] for _ in range(n)]
dp[0] = [1, 1, 1]
best = 0  # garde la meilleure valeur rencontrée

for i in range(1, n):
    prev, cur = vals[i-1], vals[i]
    if prev != cur:
        # si c'est différent, on augmente les 3 compteurs à partir d'avant
        for k in range(3):
            dp[i][k] = dp[i-1][k] + 1
    else:
        # si c'est pareil, reset un peu bizarre - j'espère que ça marche
        dp[i][0] = 1
        if dp[i-1][2] > best:
            best = dp[i-1][2]
        # on fait ça à l'envers, pas sûr pourquoi mais bon
        for k in range(2, 0, -1):
            dp[i][k] = dp[i-1][k-1] + 1

# prend la plus grosse valeur entre le dernier dp et best
print(max(max(dp[-1]), best))