def root(x):
    if x == parent[x]:
        return x
    parent[x] = root(parent[x])
    return parent[x]
def unite(x, y):
    px = root(x); py = root(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py
while 1:
    A = []; B = []
    n, m, k = map(int, raw_input().split())
    if n == m == k == 0:
        break
    parent = range(n)
    for i in xrange(m):
        u, v, w, l = raw_input().split()
        u = int(u)-1; v = int(v)-1; w = int(w)
        if l is 'A':
            A.append((w, u, v))
        else:
            B.append((w, u, v))
    A.sort(); B.sort()
    E = [[] for i in xrange(n)]
    ans = 0
    cnt = 0
    for w, u, v in A:
        if root(u) != root(v):
            unite(u, v)
            ans += w
            p = [1]
            E[u].append((v, w, p))
            E[v].append((u, w, p))
            cnt += 1
    if cnt < k:
        print -1
        continue
    used = [0]*len(B)
    rest = n-k-1
    for i, (w, u, v) in enumerate(B):
        if root(u) != root(v):
            unite(u, v)
            ans += w
            used[i] = 1
            p = [2]
            E[u].append((v, w, p))
            E[v].append((u, w, p))
            rest -= 1
            cnt += 1
    if cnt != n-1:
        print -1
        continue

    def dfs(v, s, prev):
        if v == s:
            return (-1, None)
        for i, (to, w, can) in enumerate(E[v]):
            if to == prev or can[0] == 0:
                continue
            res = dfs(to, s, v)
            if res is not None:
                if can[0] == 1:
                    return max(res, (w, can))
                else:
                    return res
        return None

    for t in xrange(rest):
        res = (10**18, None, None)
        for i, (w, u, v) in enumerate(B):
            if used[i]:
                continue
            rr = dfs(u, v, -1)
            cost, can = rr
            if cost != -1:
                res = min(res, (w - cost, i, can))
        co, i, can = res
        if i is None:
            print -1
            break
        ans += co
        can[0] = 0

        w, u, v = B[i]
        used[i] = 1
        p = [2]
        E[u].append((v, w, p))
        E[v].append((u, w, p))
    else:
        print ans
        if ans == 272:
            print A, B