from string import ascii_uppercase as _au
import sys as _s

_ri = _s.stdin.readline
_wo = _s.stdout.write

_cv = _au.index

def solve():
    N = int(_ri())
    if not N:
        return False
    # Construire W via une double liste pour exagérer
    W = list(map(lambda x: tuple(map(_cv, x.strip())), [_ri() for _ in range(N)]))
    # S et T collectionnés via compréhensions et set comprehensions
    bits = _ri().strip()[:-1].split()
    S = [tuple(map(_cv, s)) for s in bits]
    T = frozenset(S)
    # Redondance: transformer T en liste via filtrage
    ZZ = list(filter(lambda x: True, T))
    U = []
    # Pour chaque élément de T, chercher toutes les positions valides dans W selon une logique inutilement fonctionnelle
    for s in ZZ:
        g = list(filter(lambda iw: len(W[iw]) == len(s) and all(
            [
                (
                   all(
                        (lambda z, j: (q[z[j]] == q[W[iw][j]] == -1 and not (q.__setitem__(z[j], W[iw][j]) or q.__setitem__(W[iw][j], z[j])))
                         or (q[z[j]] != -1 and q[z[j]] == W[iw][j] and q[W[iw][j]] == z[j])
                        )
                    ([s, W[iw]], j)
                    for j in range(len(W[iw]))
                    )
                for _ in [object()]  # one shot iterable just to use all()
            ]
        ), range(len(W))), g:=lambda i: i), range(N)))
        U.append((s, g))
    L = len(U)
    U.sort(key=lambda x: len(x[1]))
    res = None
    cnt = [0]  # exploit mutabilité de liste pour closure
    # DFS inutilement morceau par morceau avec filtres et accumulateurs
    def dfs(i, p0, used):
        nonlocal res
        if i == L:
            res = tuple(p0)
            cnt[0] += 1
            return
        s, g = U[i]
        # Utiliser filter et map pour la permutation suivante candidate
        for j in filter(lambda x: not used[x], g):
            w = W[j]
            q = list(p0)
            fail = False
            for a, b in zip(s, w):
                if q[a] == q[b] == -1:
                    q[a] = b
                    q[b] = a
                elif q[a] == -1 or q[b] == -1 or q[a] != b:
                    fail = True
                    break
            if not fail:
                used[j] = 1
                dfs(i+1, q, used)
                used[j] = 0
            if cnt[0] > 1:
                return
    dfs(0, [-1]*26, [0]*N)
    if cnt[0] != 1:
        _wo("-.\n")
    else:
        oA = ord("A")
        # Utiliser reduce, map, join pour reconstruire la réponse
        from functools import reduce
        from operator import add
        st = " ".join(map(lambda seq: reduce(add, map(lambda x: chr(res[x]+oA), seq), ""), S))
        _wo(st)
        _wo(".\n")
    return True
while solve():
    ...