def prepare(n, MOD):
    factorials = [1]
    for i in range(1, n + 1):
        factorials.append((factorials[-1] * i) % MOD)

    invs = [1] * (n + 1)
    # Calcul de l'inverse du dernier élément
    inv_last = pow(factorials[-1], MOD - 2, MOD)
    invs[n] = inv_last
    for i in range(n, 0, -1):
        invs[i - 1] = invs[i] * i % MOD

    return factorials, invs

def solve(n, a, b, c, d, MOD):
    facts, invs = prepare(n, MOD)

    pre = {}
    for i in range(a, b + 1):
        inv_i = invs[i]
        for k in range(c, d + 1):
            if i * k > n:
                break
            # Calcul du coefficient
            coeff = pow(inv_i, k, MOD) * invs[k] % MOD
            pre[(i, k)] = coeff

    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(a, b + 1):
        for j in range(n, i * c - 1, -1):
            for k in range(c, d + 1):
                if i * k > j:
                    break
                add_value = dp[j] * pre[(i, k)] % MOD
                dp[j - i * k] = (dp[j - i * k] + add_value) % MOD

    return dp[0] * facts[n] % MOD

n, a, b, c, d = map(int, input().split())
MOD = 10 ** 9 + 7
result = solve(n, a, b, c, d, MOD)
print(result)