while True:
    n = int(input())  # nombre d'itérations ou 0 pour arrêter
    if n == 0:
        break

    s, t, b = input().split()
    base_ord = ord("A")  # pour convertir lettre en index
    blank = ord(b) - base_ord  # la position du caractère 'blank' dans l'alphabet

    # tableau dp, lignes: longueur, colonnes: positions possibles (9)
    dp = [[0 for _ in range(9)] for _ in range(n + 1)]
    dp[0][ord(s) - base_ord] = 1  # position de départ

    # transitions possibles à partir de chaque état
    transitions = {
        0: (0, 0, 1, 3),
        1: (0, 1, 2, 4),
        2: (1, 2, 2, 5),
        3: (0, 3, 4, 6),
        4: (1, 3, 5, 7),
        5: (2, 4, 5, 8),
        6: (3, 6, 6, 7),
        7: (4, 6, 7, 8),
        8: (5, 7, 8, 8)
    }

    def update(position, step):
        # ici on redistribue la probabilité selon les transitions
        for nxt in transitions[position]:
            if nxt == blank:
                # si c'est le blank, rester sur la même position et diviser par 4 (quarts)
                dp[step][position] += dp[step - 1][position] / 4
            else:
                dp[step][nxt] += dp[step - 1][position] / 4

    for i in range(1, n + 1):
        for pos in range(9):
            update(pos, i)

    # print la proba finale d’être à la position t après n étapes
    print(dp[n][ord(t) - base_ord])