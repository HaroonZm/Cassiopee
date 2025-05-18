from itertools import product
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    MOD = 10**9 + 7
    N, M = map(int, readline().split())
    S = readline().strip()
    U = [0]*M
    L = [0]*M
    mp = {}
    for i in range(10):
        mp[str(i)] = i
    for i in range(M):
        v, u = readline().split()
        mp[v] = i+10
        L[i] = len(u); U[i] = int(u)
    def root(x):
        if prt[x] == x:
            return x
        prt[x] = y = root(prt[x])
        return y
    def unite(x, y):
        px = root(x); py = root(y)
        if px < py:
            prt[py] = px
        else:
            prt[px] = py
    *T, = map(mp.__getitem__, S)
    ans = 0
    t10 = (1,)*10
    for P in product([1, 2], repeat=M):
        ok = 1
        for i in range(M):
            if P[i] > L[i]:
                ok = 0
                break
        if not ok:
            continue

        *prt, = range(10+M*2)
        l = 0; p = P[T[l]-10]-1 if T[l] >= 10 else 0
        r = N-1; q = 0
        while l < r or (l == r and q < p):
            if T[l] >= 10:
                a = T[l]*2-10+p
                if p-1 == -1:
                    l += 1; p = P[T[l]-10]-1 if T[l] >= 10 else 0
                else:
                    p -= 1
            else:
                a = T[l]
                l += 1; p = P[T[l]-10]-1 if T[l] >= 10 else 0
            if T[r] >= 10:
                b = T[r]*2-10+q
                if q+1 == P[T[r]-10]:
                    r -= 1; q = 0
                else:
                    q += 1
            else:
                b = T[r]
                r -= 1; q = 0
            unite(a, b)
        for i in range(10):
            if root(i) != i:
                ok = 0
                break
        if not ok:
            continue

        mi0 = [0]*(10+M*2)
        ma0 = [9]*(10+M*2)

        mi = [0]*(10+M*2); ma = [9]*(10+M*2)
        prt1 = prt[:]
        for Q in product([0, 1], repeat = M):
            mi[:] = mi0; ma[:] = ma0
            ok = 1
            for i in range(M):
                if P[i] < L[i] and Q[i] == 1:
                    ok = 0
                    break
            if not ok:
                continue
            prt[:] = prt1
            for i in range(10):
                mi[i] = ma[i] = i
            for i in range(M):
                if L[i] == 1:
                    v = U[i]
                    e0 = 2*i+10
                    if Q[i]:
                        unite(v, e0)
                    else:
                        ma[e0] = v-1
                else:
                    v1, v0 = divmod(U[i], 10)
                    e0 = 2*i+10; e1 = 2*i+11
                    if Q[i]:
                        unite(v1, e1)
                        ma[e0] = v0
                    else:
                        ma[e0] = 9
                        if P[i] == 2:
                            ma[e1] = v1-1; mi[e1] = 1
            for i in range(10+2*M):
                a = root(i)
                mi[a] = max(mi[a], mi[i])
                ma[a] = min(ma[a], ma[i])
            for i in range(10):
                if root(i) != i or not mi[i] == i == ma[i]:
                    ok = 0
                    break
            if not ok:
                continue

            res = 1
            for i in range(M):
                e0 = 2*i+10; e1 = 2*i+11
                if P[i] == 2:
                    if root(e1) == e1:
                        if not mi[e1] <= ma[e1]:
                            res = 0
                            break
                        res = res * (ma[e1] - mi[e1] + 1) % MOD
                if root(e0) == e0:
                    if not mi[e0] <= ma[e0]:
                        res = 0
                        break
                    res = res * (ma[e0] - mi[e0] + 1) % MOD
            ans += res
    ans %= MOD
    write("%d\n" % ans)
solve()