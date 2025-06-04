# Bon, ça va être du sport... Quelques modifs / ajouts pour humaniser tout ça

N, P = map(int, input().split()) # nombre de trucs, et P c'est le budget ou un truc du genre ?
xs = []
ys = []
dp = [[[10 ** 9 for _ in range(N + 1)] for _ in range(N + 1)] for _ in range(N + 1)] # ouch, ça fait beaucoup. On verra bien.
memo = [[0] * (N + 1) for _ in range(N + 1)] # pas sûr, on stocke quoi ici... bref

for i in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y) # coordonnées ? Quantités ? On devine pas toujours :|

# ok, ça prépare un genre de tableau mémoire...
for start in range(N):
    preuse = 0
    for now in range(start, N + 1):
        if now == start:
            preuse = 0
            memo[start][now] = 0
        else:
            nx = max(0, xs[now - 1] - preuse) # ça doit être la diff à consommer ?
            preuse = max(0, ys[now - 1] - nx)
            memo[start][now] = memo[start][now - 1] + preuse # cumul

dp[0][0][0] = 0
for now in range(N):
    for l in range(now + 1): # l... pour left ou pour last ? Bon
        for score in range(N): # score comme dans on compte les points !
            # on essaye d'ajouter un "score"
            dp[now + 1][l][score + 1] = min(dp[now + 1][l][score + 1],
                                            dp[now][l][score] + memo[l][now + 1] - memo[l][now])
            # ou sinon, on reset le l je pense (?)
            dp[now + 1][now + 1][score] = min(dp[now + 1][now + 1][score],
                                              dp[now][l][score])

# on cherche le "score" max tel que le coût reste OK
ans = 0
for l in range(N + 1):
    for score in range(N):
        if dp[N][l][score] <= P:
            if score > ans:
                ans = score

print(ans) # et voilà, on croise les doigts...