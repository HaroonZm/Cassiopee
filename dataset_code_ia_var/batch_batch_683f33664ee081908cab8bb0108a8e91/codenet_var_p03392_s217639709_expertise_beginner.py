def solve(s):
    MOD = 998244353

    n = len(s)
    # Cas pour 2 lettres
    if n == 2:
        if s[0] == s[1]:
            return 1
        else:
            return 2
    # Cas pour 3 lettres
    if n == 3:
        if s[0] == s[1] and s[1] == s[2]:
            return 1
        elif s[0] == s[1] or s[1] == s[2]:
            return 6
        elif s[0] == s[2]:
            return 7
        else:
            return 3

    same = True
    for i in range(1, n):
        if s[i] != s[0]:
            same = False
            break
    if same:
        return 1

    # Préparation du tableau dp à 3 dimensions
    dp = []
    for i in range(2):
        layer = []
        for j in range(3):
            layer.append([0, 0, 0])
        dp.append(layer)
    dp[0][0][0] = 1
    dp[0][1][1] = 1
    dp[0][2][2] = 1

    for t in range(n - 1):
        ndp = []
        for i in range(2):
            layer = []
            for j in range(3):
                layer.append([0, 0, 0])
            ndp.append(layer)
        # Copie des transitions du code avancé de façon basique
        ndp[0][0][0] = (dp[0][1][0] + dp[0][2][0]) % MOD
        ndp[0][0][1] = (dp[0][1][1] + dp[0][2][1]) % MOD
        ndp[0][0][2] = (dp[0][1][2] + dp[0][2][2]) % MOD
        ndp[0][1][0] = (dp[0][0][2] + dp[0][2][2]) % MOD
        ndp[0][1][1] = (dp[0][0][0] + dp[0][2][0]) % MOD
        ndp[0][1][2] = (dp[0][0][1] + dp[0][2][1]) % MOD
        ndp[0][2][0] = (dp[0][0][1] + dp[0][1][1]) % MOD
        ndp[0][2][1] = (dp[0][0][2] + dp[0][1][2]) % MOD
        ndp[0][2][2] = (dp[0][0][0] + dp[0][1][0]) % MOD
        ndp[1][0][0] = (dp[0][0][0] + dp[1][0][0] + dp[1][1][0] + dp[1][2][0]) % MOD
        ndp[1][0][1] = (dp[0][0][1] + dp[1][0][1] + dp[1][1][1] + dp[1][2][1]) % MOD
        ndp[1][0][2] = (dp[0][0][2] + dp[1][0][2] + dp[1][1][2] + dp[1][2][2]) % MOD
        ndp[1][1][0] = (dp[0][1][2] + dp[1][0][2] + dp[1][1][2] + dp[1][2][2]) % MOD
        ndp[1][1][1] = (dp[0][1][0] + dp[1][0][0] + dp[1][1][0] + dp[1][2][0]) % MOD
        ndp[1][1][2] = (dp[0][1][1] + dp[1][0][1] + dp[1][1][1] + dp[1][2][1]) % MOD
        ndp[1][2][0] = (dp[0][2][1] + dp[1][0][1] + dp[1][1][1] + dp[1][2][1]) % MOD
        ndp[1][2][1] = (dp[0][2][2] + dp[1][0][2] + dp[1][1][2] + dp[1][2][2]) % MOD
        ndp[1][2][2] = (dp[0][2][0] + dp[1][0][0] + dp[1][1][0] + dp[1][2][0]) % MOD
        dp = ndp

    s_ascii_sum = 0
    for c in s:
        s_ascii_sum += ord(c)
    s_mod = s_ascii_sum % 3

    total = 0
    for x in range(3):
        total += dp[1][x][s_mod]
    # Vérifier si tous les caractères sont différents deux à deux
    all_diff = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            all_diff = False
            break
    if all_diff:
        total += 1
    return total % MOD

s = input()
print(solve(s))