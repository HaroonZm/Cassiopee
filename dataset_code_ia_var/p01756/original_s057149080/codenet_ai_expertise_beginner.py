import sys

def solve():
    base = 37
    MOD = 10**9 + 9
    S = sys.stdin.readline().strip()
    L = len(S)

    # Pré-calculer les hash-prefixes
    H = [0] * (L + 1)
    v = 0
    ca = ord('a')
    for i in range(L):
        v = (v * base + (ord(S[i]) - ca)) % MOD
        H[i + 1] = v

    M = int(sys.stdin.readline())
    Q = []
    s = {}

    # Lire les requêtes et fabriquer l'ensemble des hash recherchés par taille
    for _ in range(M):
        x, y = sys.stdin.readline().split()
        # Hash de x
        v0 = 0
        for c in x:
            v0 = (v0 * base + (ord(c) - ca)) % MOD
        if len(x) not in s:
            s[len(x)] = set()
        s[len(x)].add(v0)
        # Hash de y
        v1 = 0
        for c in y:
            v1 = (v1 * base + (ord(c) - ca)) % MOD
        if len(y) not in s:
            s[len(y)] = set()
        s[len(y)].add(v1)
        Q.append((len(x), v0, len(y), v1))

    # Chercher les premiers et derniers indices où chaque hash apparait
    fvs = {}
    lvs = {}
    for l in s:
        vs = s[l]
        p = pow(base, l, MOD)
        fs = {}
        ls = {}
        for i in range(L - l + 1):
            v = (H[i + l] - (H[i] * p) % MOD) % MOD
            if v not in fs:
                fs[v] = i
            ls[v] = i
        fv = {}
        lv = {}
        for v in vs:
            if v in fs:
                fv[v] = fs[v]
            else:
                fv[v] = L + 1
            if v in ls:
                lv[v] = ls[v]
            else:
                lv[v] = -1
        fvs[l] = fv
        lvs[l] = lv

    # Répondre aux requêtes
    for lx, x, ly, y in Q:
        p0 = fvs[lx][x]
        p1 = lvs[ly][y]
        if p0 <= p1 and p0 + lx <= p1 + ly:
            print(p1 + ly - p0)
        else:
            print(0)

solve()