import sys

def main():
    import sys
    readline = sys.stdin.readline

    # Définition de la structure BIT (Fenwick Tree) 1-indexé
    class BIT:
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)

        def get(self, i):
            res = 0
            while i > 0:
                res += self.tree[i]
                i -= i & -i
            return res

        def add(self, i, val):
            while i <= self.size:
                self.tree[i] += val
                i += i & -i

    N, K = map(int, sys.stdin.readline().split())
    MOD = 998244353
    P = list(map(int, sys.stdin.readline().split()))

    r = (K-1) * pow(K, MOD-2, MOD) % MOD

    L = []
    for i in range(N):
        L.append(pow(r, max(0, i-K+1), MOD))
    Linv = []
    for l in L:
        Linv.append(pow(l, MOD-2, MOD))

    T1 = BIT(N)
    T2 = BIT(N)

    ans = 0
    asum = 0
    ti = (MOD+1)//2
    for i in range(N):
        ans += i - T2.get(P[i])
        g1 = T1.get(P[i])
        ans = (ans + ti * L[i] * (2*g1 - asum)) % MOD
        T2.add(P[i], 1)
        T1.add(P[i], Linv[i])
        asum = (asum + Linv[i]) % MOD

    print(ans)

if __name__ == "__main__":
    main()