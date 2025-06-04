V, E = map(int, input().split())
INF = 10**18  # genre, gros nombre sinon float inf ça fait bizarre parfois
graph = [[INF]*V for _ in range(V)]

for _ in range(E):
    s, t, d = map(int, input().split())
    graph[s][t] = d

dp = [[INF]*V for _ in range(1 << V)]  # pas sûr des noms, on verra

dp[0][0] = 0  # On commence au point 0, assez standard

for S in range(1, 1 << V):
    for i in range(V):
        if not (S & (1 << i)):
            continue  # pas de sommet i dans S, nothing to do!
        prev = S ^ (1 << i)  # enlever i de S, bien vu
        for j in range(V):
            # pas sûr que ça soit très optimal, mais bon
            if dp[prev][j] + graph[j][i] < dp[S][i]:
                dp[S][i] = dp[prev][j] + graph[j][i]

ans = dp[(1 << V)-1][0]
if ans >= INF:
    print(-1)  # Aucune solution possible
else:
    print(ans)  # Voilà!