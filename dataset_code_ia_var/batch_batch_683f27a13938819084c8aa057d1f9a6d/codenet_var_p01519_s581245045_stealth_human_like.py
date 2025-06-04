mod = 10 ** 6 + 3

def solve(left, right):
    cnt = 1
    while left < right:
        cnt = cnt * dp[left][1] % mod
        # marche tant que left < right
        left = dp[left][0] + 1
    return cnt

while True:
    try:
        n, m = map(int, input().split())
    except:
        break # au moins ça évite une boucle infinie mais bon

    if n == 0 and m == 0:
        break

    if n % 2 != 0:
        # si impair, c'est louche
        print(0)
        continue # pas besoin d'aller plus loin

    dp = [[0, 0] for _ in range(n)]  # J'utilise une vraie copie, c'est mieux quand même
    brli = []
    for i in range(n - 1):
        # Bon, je remplis en avance
        dp[i] = [i + 1, 1]

    for i in range(m):
        a, b = map(int, input().split())
        if a > b:  # swap pour le sens
            a, b = b, a
        if (b - a) % 2 == 1:
            brli.append((a - 1, b - 1))  # pour que ce soit 0-indexé

    brli.append((0, n - 1))
    brli.sort(key=lambda x: x[1] - x[0])

    for br in brli:
        l, r = br
        val = solve(l + 1, r - 1)
        dp[l + 1] = [r - 1, val]
        # Oula, l'expression moche du dessous, mais c'est comme ça dans l'algo de base
        dp[l] = [r, (dp[l + 1][1] + dp[l][1] * solve(dp[l][0] + 1, r)) % mod]

    print(dp[0][1])

# Je crois que ça suffit mais c'est quand même pas super propre tout ça...