MOD = 10 ** 9 + 7

def prepare(n):
    modFacts = [1] * (n + 1)
    for i in range(1, n + 1):
        modFacts[i] = (modFacts[i - 1] * i) % MOD

    invs = [1] * (n + 1)
    invs[n] = pow(modFacts[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        invs[i - 1] = (invs[i] * i) % MOD

    return modFacts, invs

def f(i, j):
    num = modFacts[i + j]
    denom = (invs[i] * invs[j]) % MOD
    return (num * denom) % MOD

def g(r1, r2, y):
    total = 0
    for x in range(r1, r2 + 1):
        total = (total + f(x + 1, y)) % MOD
    return total

r1, c1, r2, c2 = map(int, input().split())
N = max(r1, r2, c1, c2) * 2 + 2
modFacts, invs = prepare(N)

ans = g(r1, r2, c2) - g(r1, r2, c1 - 1)
print(ans % MOD)