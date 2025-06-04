def find_root(x):
    if parent[x] == x:
        return x
    parent[x] = find_root(parent[x])
    return parent[x]

def union(x, y):
    rx = find_root(x)
    ry = find_root(y)
    if rx < ry:
        parent[ry] = rx
    else:
        parent[rx] = ry

while True:
    A = []
    B = []
    nmk = raw_input().split()
    n = int(nmk[0])
    m = int(nmk[1])
    k = int(nmk[2])
    if n == 0 and m == 0 and k == 0:
        break

    parent = []
    for i in range(n):
        parent.append(i)

    for i in range(m):
        parts = raw_input().split()
        u = int(parts[0]) - 1
        v = int(parts[1]) - 1
        w = int(parts[2])
        l = parts[3]
        if l == 'A':
            A.append((w, u, v))
        else:
            B.append((w, u, v))
    A.sort()
    B.sort()
    E = []
    for i in range(n):
        E.append([])

    ans = 0
    cnt = 0

    for i in range(len(A)):
        w, u, v = A[i]
        if find_root(u) != find_root(v):
            union(u, v)
            ans = ans + w
            p = [1]
            E[u].append((v, w, p))
            E[v].append((u, w, p))
            cnt = cnt + 1

    if cnt < k:
        print -1
        continue

    used = []
    for i in range(len(B)):
        used.append(0)
    rest = n - k - 1

    for i in range(len(B)):
        w, u, v = B[i]
        if find_root(u) != find_root(v):
            union(u, v)
            ans = ans + w
            used[i] = 1
            p = [2]
            E[u].append((v, w, p))
            E[v].append((u, w, p))
            rest = rest - 1
            cnt = cnt + 1

    if cnt != n - 1:
        print -1
        continue

    def dfs(v, target, prev):
        if v == target:
            return (-1, None)
        for i in range(len(E[v])):
            to, w, can = E[v][i]
            if to == prev or can[0] == 0:
                continue
            result = dfs(to, target, v)
            if result is not None:
                if can[0] == 1:
                    if result[0] > w:
                        return result
                    else:
                        return (w, can)
                else:
                    return result
        return None

    for t in range(rest):
        min_diff = 10**18
        idx = None
        can_ptr = None
        for i in range(len(B)):
            w, u, v = B[i]
            if used[i]:
                continue
            r = dfs(u, v, -1)
            if r is not None:
                cost, can = r
                if cost != -1:
                    if w - cost < min_diff:
                        min_diff = w - cost
                        idx = i
                        can_ptr = can
        if idx is None:
            print -1
            break
        ans = ans + min_diff
        can_ptr[0] = 0

        w, u, v = B[idx]
        used[idx] = 1
        p = [2]
        E[u].append((v, w, p))
        E[v].append((u, w, p))
    else:
        print ans
        if ans == 272:
            print A, B