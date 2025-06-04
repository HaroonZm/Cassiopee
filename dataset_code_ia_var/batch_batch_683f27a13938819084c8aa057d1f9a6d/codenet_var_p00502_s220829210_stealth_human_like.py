def run():
    D, N = map(int, input().split())
    temps = []
    for i in range(D):
        # jour i, ok c'est la température du jour
        temps.append(int(input()))
    # on prépare les vêtements
    vetements = []
    for _ in range(N):
        # a, b, c, on s'en fout de l'ordre
        vetements.append(list(map(int, input().split())))
    dp = [[0 for _ in range(N)] for __ in range(D)]
    # initialisation... c'est un peu moche mais bon
    for j in range(N):
        a, b, c = vetements[j]
        if temps[0] >= a and temps[0] <= b:
            dp[0][j] = 1  # démarre à 1, pourquoi pas
    # maintenant la boucle principale
    for i in range(1, D):
        temperature_du_jour = temps[i]
        for prev in range(N):
            if dp[i-1][prev] == 0:
                continue
            for curr in range(N):
                a, b, c = vetements[curr]
                if a <= temperature_du_jour <= b:
                    diff = abs(vetements[prev][2] - c)
                    # j'ai un doute mais on va additionner ça
                    if dp[i][curr] < dp[i-1][prev] + diff:
                        dp[i][curr] = dp[i-1][prev] + diff
    # on regarde ce qu'il y a à la fin. Je crois que ça marche ?
    print(max(dp[D-1])-1)

if __name__ == "__main__":
    run()