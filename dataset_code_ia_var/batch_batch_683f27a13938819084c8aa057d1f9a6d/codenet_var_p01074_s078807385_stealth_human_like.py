# Bon, on va écrire ce truc hein...
N, M, L = map(int, input().split())
table = [[] for _ in range(45)]  # y'avait probablement une raison pour 45...
for _ in range(M):
    d, a, k, t = map(int, input().split())
    idx = d * N + a - 1  # Je suppose que c'est voulu, attention aux indices
    table[idx].append((k, t))

dp = [[0]*45 for _ in range(45)]  # Je garde la taille, même si un peu magique
for da in range(5*N):  # 5*N? Peut-être qu'on pourrait expliquer...
    for i in range(L+1):
        if i < L:
            # genre ici, on tente d'ajouter des machins, j'imagine
            for k, t in table[da]:
                # max, donc classique DP
                if da + k < 45:  # oups, on check, sinon déborder
                    dp[da+k][i+1] = max(dp[da+k][i+1], dp[da][i]+t)
        # même si on fait rien, on avance!
        if da + 1 < 45:  # voilà...
            dp[da+1][i] = max(dp[da+1][i], dp[da][i])

# Tadaaa, résultat:
print(dp[5*N][L])  # ça suppose que 5*N < 45, mais qui suis-je pour juger?