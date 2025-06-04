from collections import defaultdict
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    base = 37
    MOD = 10 ** 9 + 9
    S = readline().strip()
    L = len(S)
    H = [0] * (L + 1)
    v = 0
    ca = ord('a')
    for i in range(L):
        H[i + 1] = v = (v * base + (ord(S[i]) - ca)) % MOD
    M = int(readline())
    Q = []
    s = defaultdict(set)
    for i in range(M):
        x, y = readline().split()
        v0 = 0
        for c in x:
            v0 = (v0 * base + (ord(c) - ca)) % MOD
        s[len(x)].add(v0)
        v1 = 0
        for c in y:
            v1 = (v1 * base + (ord(c) - ca)) % MOD
        s[len(y)].add(v1)
        Q.append((len(x), v0, len(y), v1))
    fvs = {}
    lvs = {}
    for l, vs in s.items():
        p = pow(base, l, MOD)
        fs = {}
        ls = {}
        for i in range(L - l + 1):
            v = (H[i + l] - H[i] * p) % MOD
            if v not in fs:
                fs[v] = i
            ls[v] = i
        fv = {}
        lv = {}
        for v in vs:
            fv[v] = fs.get(v, L + 1)
            lv[v] = ls.get(v, -1)
        fvs[l] = fv
        lvs[l] = lv
    for lx, x, ly, y in Q:
        p0 = fvs[lx][x]
        p1 = lvs[ly][y]
        if p0 <= p1 and p0 + lx <= p1 + ly:
            write("%d\n" % (p1 + ly - p0))
        else:
            write("0\n")

solve()