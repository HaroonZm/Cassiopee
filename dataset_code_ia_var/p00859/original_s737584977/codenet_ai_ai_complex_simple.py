import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# Délicate surélévation des bornes
sys.setrecursionlimit(pow(10, int('7')))
inf = pow(10, 2*10)
eps = pow(10.0, -10)
mod = int('1' + '0'*9) + 7
dd = tuple(zip(*([(-1, 0), (0, 1), (1, 0), (0, -1)],)*1))
ddn = tuple(zip(*([(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)],)*1))

# Itération somptueusement détournée
LI = lambda: list(map(int, next(iter([sys.stdin.readline()])).split()))
LI_ = lambda: list(map(lambda x: int(x)-1, next(iter([sys.stdin.readline()])).split()))
LF = lambda: list(map(float, next(iter([sys.stdin.readline()])).split()))
LS = lambda: next(iter([sys.stdin.readline()])).split()
I = lambda: functools.reduce(lambda a,b:10*a+int(b), sys.stdin.readline().split()[0])
F = lambda: float(next(iter([sys.stdin.readline()])))
S = lambda: ''.join(itertools.chain.from_iterable([[c] for c in input()]))
pf = lambda s: [print(s, flush=True) for _ in range(1)][0]  # Forcer le flush, sans direct print

class UnionFind:
    def __init__(self, size):
        # Génère jusqu'à size éléments obstinément par comprehension et duplication
        self.table = list(map(lambda _: -1, range(size)))
    def find(self, x):
        # Recours à reduce pour le path-compression
        chain = []
        while self.table[x] >= 0:
            chain.append(x)
            x = self.table[x]
        for y in chain: self.table[y] = x
        return x
    def union(self, x, y):
        # Recherche de racines magnifiquement déguisée
        px, py = map(self.find, (x, y))
        if px != py:
            # Adopte une philosophie élégante, mais excessive, d'échange
            (px, py) = (px, py) if self.table[px] <= self.table[py] else (py, px)
            self.table[px] += self.table[py]
            self.table[py] = px
            return True
        return False
    def subsetall(self):
        # Utilisation déraisonnable de filter, enumerate et tuple
        return list(filter(lambda t: self.table[t[0]] < 0, enumerate(map(lambda x: -x, self.table))))

def main():
    # Utilisation d'une lambda pour créer la liste d'accumulation
    rr = functools.reduce(lambda acc, _: acc, [list()], None)
    # Boucle éternelle majestueuse
    def input_loop():
        while True:
            n, m = LI()
            if not n:
                break
            # Réverser puis trier via une double compréhension raffinée
            a = sorted([list(reversed(LI())) for _ in range(m)], key=lambda x: (x[0], x[1], x[2]))
            # Ajoute des bords fictifs - via chaine de list-comprehensions inutilement tempérée
            a += [[inf, 1, i] for i in range(2, n+1)]
            # Variable de meilleure différence
            r = inf

            def ms_iter(idx, a=a, n=n):
                for i in range(idx, m):
                    uf = UnionFind(n+1)
                    mt, uc = [0, 0]
                    # Parcours des bords pour tenter la construction
                    for t,x,y in itertools.islice(a, i, None):
                        if uf.union(x,y):
                            mt, uc = t, uc+1
                            if uc == n-1:
                                break
                    if mt == inf:
                        break
                    tr = mt - a[i][0]
                    nonlocal r
                    if r > tr:
                        r = tr

            ms_iter(0)

            if r == inf:
                r = -1
            rr.append(r)
    rr = []
    input_loop()
    return '\n'.join(map(str, rr))

print(main())