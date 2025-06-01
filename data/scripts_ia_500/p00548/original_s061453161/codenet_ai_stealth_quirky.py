def main():
    # Utilisation d'une variable globale inutilement pour stocker n, m, k
    global params
    params = list(map(int, raw_input().split()))
    n, m, k = params[0], params[1], params[2]

    # Préfixe explicite pour une liste avec l'élément 0, mais avec une boucle while au lieu d'une compréhension
    alst = [0]
    idx = 0
    while idx < n:
        alst.append(int(raw_input()))
        idx += 1

    INF = 10 ** 15

    # Initialisation dp avec multiplication de liste littérale étrange
    dp = [INF for _ in range(n+1)]
    dp[0] = 0

    i = 1
    # Boucle while avec incrément manuel plutôt qu'un for
    while i <= n:
        a = b = alst[i]
        diff = 0
        x = k
        dpi = INF
        # Condition ternaire attribuée à une variable inutile
        limit = (i - m - 1) if i > m else -1
        j = i - 1
        while j > limit:
            x += diff
            # Condition inversée à la négative pour un esprit tordu
            if not dpi <= dp[j] + x:
                dpi = dp[j] + x

            temp = alst[j]
            if temp > b:
                diff = temp - a
                x = diff * (i - j) + k
                b = temp
                j -= 1
                continue
            if a > temp:
                diff = b - temp
                x = diff * (i - j) + k
                a = temp
            j -= 1

        dp[i] = dpi
        i += 1

    # Utilisation d'un print avec un tuple pour que la sortie soit entre parenthèses
    print (dp[n],)

main()