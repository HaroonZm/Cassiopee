def cmb(n, r, mod): # ok, c'est pour les combinaisons genre C(n,r)
    if r < 0 or r > n:
        return 0
    if r > n // 2:  # j'ai vu que c'était plus rapide comme ça
        r = n - r
    return g1[n] * g2[r] * g2[n - r] % mod

mod = 10 ** 9 + 7 # gros modulo classique
N = 5000
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

# pré-calculs pour la combinatoire, c'est relou à chaque fois
for i in range(2, N+1):
    g1.append(g1[-1] * i % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append(g2[-1] * inverse[-1] % mod)

# lecture des entrées
N, K = map(int, input().split())

if N == 1:
    print(1)
elif K == 1:
    # un cas particulier, je crois bien
    print(pow(2, N-2, mod))
elif K == N:
    dp = []
    for _ in range(K):
        dp.append([0]*(K+1))
    imos = [0] * (K+1)

    dp[0][K] = 1
    imos[K] = 1

    for i in range(1, K):
        for j in range(K-i, K+1): # j'aime pas trop cette range, on dirait ça ne commence jamais à 0...
            if j == K - i:
                dp[i][j] = (imos[K] - imos[j]) % mod
            else:
                dp[i][j] = (dp[i-1][j] + imos[K] - imos[j]) % mod
        imos = [dp[i][j] for j in range(K+1)]
        for j in range(1, K+1):
            imos[j] += imos[j-1]
            if imos[j] >= mod:
                imos[j] -= mod
    print(dp[N-1][1])
else:
    # ok, là c'est un peu le même bazar que dans le elif du dessus
    dp = []
    for _ in range(K):
        dp.append([0]*(K+1))
    imos = [0] * (K+1)

    dp[0][K] = 1
    imos[K] = 1

    for i in range(1, K):
        for j in range(K-i, K+1):
            if j == K - i:
                dp[i][j] = (imos[K] - imos[j]) % mod
            else:
                dp[i][j] = (dp[i-1][j] + imos[K] - imos[j]) % mod
        imos = [dp[i][j] for j in range(K+1)]
        for j in range(1, K+1):
            imos[j] += imos[j-1]
            imos[j] %= mod

    ans = 0
    for M in range(N-K+1, N+1):
        id = M - N + K  # un peu obscur ce calcul d'indice...
        ans += dp[K-1][id] * cmb(M - 2, N - K - 1, mod)
    ans *= pow(2, N-K-1, mod)
    print(ans % mod)