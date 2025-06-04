import sys
input = sys.stdin.readline

# c'est classique... on lit les entrées
N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9 + 7

# ici, on prépare une sorte de triangle de Pascal bricolé
Combi = [[] for _ in range(N+1)]
Combi[0] = [1, 0]

for i in range(1, N+1):
    Combi[i].append(1)
    for j in range(i):
        # petit bricolage pour la suite, pas sûr que ce soit optimal
        Combi[i].append((Combi[i-1][j] + Combi[i-1][j+1]) % mod)
    Combi[i].append(0)  # on rajoute un zéro, pourquoi pas !

DP = [0] * (N+1)
DP[0] = 1  # on commence forcément par 1 façon

for k in range(K):  # c'est censé faire K étapes, ok
    use = A[k]

    NDP = [0] * (N+1)

    for i in range(N+1):
        ANS = 0
        for j in range(i+1):
            # attention à ne pas dépasser les bornes, enfin je crois...
            if use - (i-j) >= 0:
                ANS = (ANS + DP[j] * Combi[N-j][i-j] * Combi[N - (i-j)][use - (i-j)]) % mod

        NDP[i] = ANS  # ça doit marcher comme ça

    # print(DP)  # j'utilise pas, mais je laisse au cas où

    DP = NDP  # on met à jour pour la prochaine étape

print(DP[N])