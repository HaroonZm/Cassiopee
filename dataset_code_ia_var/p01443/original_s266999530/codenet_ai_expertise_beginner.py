import sys

sys.setrecursionlimit(10000000)

# Quelques constantes utiles
inf = 10**20
eps = 1.0 / (10**13)
mod = 10**9+7

# Déplacements sur une grille
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    print(s, flush=True)

class BIT:
    def __init__(self, n, p):
        self.p = p
        size = 1
        while size < n:
            size *= 2
        self.N = size
        self.BITdata = [0]*(self.N+2)

    def find(self, i):
        res = 0
        while i > 0:
            res = (res + self.BITdata[i]) % self.p
            i -= (i & -i)
        return res

    def update(self, i, x):
        while i < len(self.BITdata):
            self.BITdata[i] = (self.BITdata[i] + x) % self.p
            i += (i & -i)

    def total(self):
        # total des éléments (jusqu'au dernier index utilisé)
        return self.find(self.N+1)

    def query(self, a, b):
        return (self.find(b) - self.find(a)) % self.p

def main():
    rr = []

    def f(a, b, p):
        # Créer la liste des valeurs et leur ordre trié par string
        aa = list(range(a, b+1))
        aa_str = list(map(str, aa))
        aa_sorted = sorted(aa_str)
        l = len(aa)
        d = {}
        for idx in range(l):
            d[int(aa_sorted[idx])] = idx

        segment = BIT(l+2, p)

        for c in aa:
            pos = d[c]+1
            current = segment.find(pos)
            segment.update(pos, (current + 1) % p)

        return segment.total() % p

    while True:
        inputs = LI()
        if not inputs:
            continue
        n, m, l = inputs
        if n == 0:
            break
        rr.append(f(n, m, l))
    return "\n".join(str(x) for x in rr)

print(main())