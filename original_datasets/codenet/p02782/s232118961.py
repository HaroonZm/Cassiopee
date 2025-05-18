MOD = 10 ** 9 + 7

def prepare(n):
    global MOD
    modFacts = [0] * (n + 1)
    modFacts[0] = 1
    for i in range(n):
        modFacts[i + 1] = (modFacts[i] * (i + 1)) % MOD

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], MOD - 2, MOD)
    for i in range(n, 1, -1):
        invs[i - 1] = (invs[i] * i) % MOD

    return modFacts, invs

def f(i, j):
    Fij = modFacts[i + j]
    Ii = invs[i]
    Ij = invs[j]
    rst = (Fij * Ii * Ij) % MOD
    return rst

def g(r1, r2, y):
    rst = 0
    for x in range(r1, r2 + 1):
        rst += f(x + 1, y)
        rst %= MOD
    return rst

r1, c1, r2, c2 = map(int, input().split())
modFacts, invs = prepare(max(r1, c1, r2, c2) * 2 + 1)

ans = g(r1, r2, c2) - g(r1, r2, c1 - 1)

print(ans % MOD)