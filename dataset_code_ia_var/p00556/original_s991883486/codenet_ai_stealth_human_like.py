def main():
    # lecture de N et M, rien de fou ici
    N, M = map(int, input().split())
    # Je construis la liste a, attention -1 pour la base zéro
    a = []
    for _ in range(N):
        a.append(int(input())-1)
    # initialisation: sum par couleur, cnt par couleur
    sumtab = []
    for _ in range(20):
        sumtab.append([0]*N)
    cnt = [0]*20
    ans_bit = 0
    # le traitement principal
    for i in range(N):
        ans_bit = ans_bit | (1 << a[i])
        cnt[a[i]] += 1
        sumtab[a[i]][i] += 1  # incrément étrange mais utile
        if i > 0:
            for j in range(20):
                sumtab[j][i] += sumtab[j][i-1]
    # DP pour le bitmask, je garde tout ça dans un grand tableau
    BIG = 10**9
    dp = [BIG] * (1 << 20)
    dp[0] = 0
    for bit in range(1 << 20):
        if dp[bit] == BIG:  # commencer seulement si déjà atteint
            continue
        v = 0
        # calculer combien de ceux déjà utilisés?
        for used in range(20):
            if (bit >> used) & 1:
                v += cnt[used]
        for use in range(20):
            if cnt[use] == 0:  # couleur pas présente
                continue
            if (bit >> use) & 1:
                continue
            w = v + cnt[use]
            not_move = sumtab[use][w-1]  # combien déjà bien placés
            if v > 0:
                not_move -= sumtab[use][v-1]
            move = cnt[use] - not_move
            mask = bit | (1 << use)
            if dp[mask] > dp[bit] + move:  # juste au cas où, min classique
                dp[mask] = dp[bit] + move
    print(dp[ans_bit])
    

if __name__ == '__main__':
    main()