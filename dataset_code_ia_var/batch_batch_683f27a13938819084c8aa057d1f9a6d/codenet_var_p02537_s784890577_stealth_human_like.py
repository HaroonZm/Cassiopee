import sys
import typing

# C'est pas la plus élégante, mais bon...
def input():
    return sys.stdin.readline()

N_K = input().split()
N, K = map(int, N_K)
A = []
for idx in range(N):
    A.append(int(input()))

# SegTree etc, classique - je laisse les noms comme ça, pas envie de tout changer.
def _ceil_pow2(n):
    x = 0
    # on cherche la plus petite puissance de 2 >= n
    while (1 << x) < n:
        x += 1
    return x

def _bsf(n):
    x = 0
    # bits de poids faibles, hein
    while n % 2 == 0 and n:
        x += 1
        n //= 2
    return x

class SegTree:
    def __init__(self, op, e, v):
        self._op = op
        self._e = e
        # supporte int ou list, je préfère les listes
        if type(v) is int:
            v = [e for _ in range(v)]
        self._n = len(v)
        self._log = _ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p, x):
        if p < 0 or p >= self._n:
            raise Exception('bad idx')
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        # bon, j'aime pas trop ces noms mais pas grave
        assert l <= r <= self._n
        sml = self._e
        smr = self._e
        l += self._size
        r += self._size
        while l < r:
            if l % 2 == 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l //= 2; r //= 2
        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        # maj la valeur du noeud
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])


MAX_A = 300005  # j'arrondis comme ça, c'est suffisant large je pense
# un peu oldschool: tableau/DP statique
dp = [0] * MAX_A

segtree = SegTree(max, 0, MAX_A)  # on part sur max, unité 0

for i in range(N):
    x = A[i]
    l = max(0, x - K)
    r = min(MAX_A, x + K + 1)
    cur = segtree.prod(l, r) + 1  # on cherche le meilleur dans [l, r)
    segtree.set(x, cur)

# résultat: plus long sous-ensemble croissant avec diff max K
print(segtree.prod(0, MAX_A))