import sys
from collections import deque

def solve():
    MOD = 10**9 + 9

    n, m = map(int, sys.stdin.readline().split())
    K = 3 * n

    # Calcul des factorielles et inverses
    fact = [1] * (K + 1)
    rfact = [1] * (K + 1)
    for i in range(1, K + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    rfact[K] = pow(fact[K], MOD - 2, MOD)
    for i in range(K, 0, -1):
        rfact[i - 1] = (rfact[i] * i) % MOD

    # Calcul puissance inverse de 6
    pr6 = [1] * (n + 1)
    inv6 = pow(6, MOD - 2, MOD)
    for i in range(1, n + 1):
        pr6[i] = (pr6[i - 1] * inv6) % MOD

    # Lecture du graphe et typage des arêtes
    mp = {}
    next_idx = 0
    G = [[] for _ in range(m * 2)]
    E = []
    m2 = 0

    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if a not in mp:
            mp[a] = next_idx
            next_idx += 1
        if b not in mp:
            mp[b] = next_idx
            next_idx += 1
        ia = mp[a]
        ib = mp[b]
        if c == 0:
            G[ia].append(ib)
            G[ib].append(ia)
        else:
            E.append((ia, ib))
            m2 += 1

    L = next_idx
    lb = [-1] * L
    sz = []
    zz = []
    cc = [0, 0, 0]
    used = [False] * (1 << m2)
    visited = [False] * L

    # Recherche des composantes connexes
    component = 0
    for i in range(L):
        if visited[i]:
            continue
        queue = deque()
        queue.append(i)
        visited[i] = True
        vs = []
        while queue:
            u = queue.popleft()
            vs.append(u)
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        size = len(vs)
        if size > 3:
            print(0)
            return
        for v in vs:
            lb[v] = component
        sz.append(size)
        zz.append(vs)
        cc[size - 1] += 1
        component += 1

    answer = 0

    # Parcours récursif pour générer les configurations valides
    def dfs(state, depth, lb, cc):
        nonlocal answer
        if used[state]:
            return
        used[state] = True
        x = cc[0] + (K - L)
        y = cc[1]
        if x >= y:
            k = (x - y) // 3
            val = fact[x] * pr6[k] % MOD * rfact[k] % MOD
            if depth % 2 == 0:
                answer = (answer + val) % MOD
            else:
                answer = (answer - val) % MOD
        cc0 = [cc[0], cc[1], cc[2]]
        for i in range(m2):
            if (state >> i) & 1:
                continue
            a, b = E[i]
            la = lb[a]
            lb_ = lb[b]
            if la != lb_:
                sz_sum = sz[la] + sz[lb_]
                if sz_sum > 3:
                    continue
                cc0[sz[la] - 1] -= 1
                cc0[sz[lb_] - 1] -= 1
                cc0[sz_sum - 1] += 1

                prev_sz = len(sz)
                vs_merge = zz[la] + zz[lb_]

                for v in vs_merge:
                    lb[v] = prev_sz
                sz.append(sz_sum)
                zz.append(vs_merge)

                dfs(state | (1 << i), depth + 1, lb, cc0)

                for v in zz[la]:
                    lb[v] = la
                for v in zz[lb_]:
                    lb[v] = lb_
                sz.pop()
                zz.pop()
                cc0[sz_sum - 1] -= 1
                cc0[sz[la] - 1] += 1
                cc0[sz[lb_] - 1] += 1
            else:
                dfs(state | (1 << i), depth + 1, lb, cc)

    dfs(0, 0, lb[:], cc[:])
    print(answer % MOD)

solve()