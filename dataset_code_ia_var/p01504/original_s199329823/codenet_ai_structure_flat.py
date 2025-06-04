import sys
readline = sys.stdin.readline
write = sys.stdout.write

i = 1
while True:
    line = readline()
    if not line:
        break
    N_T_K = list(map(int, line.split()))
    if len(N_T_K) < 3:
        continue
    N, T, K = N_T_K
    if N == 0 and T == 0 and K == 0:
        break
    G = []
    E = []
    res = 0
    for _ in range(N-1):
        a, b, c = map(int, readline().split())
        res += c
        E.append((c, a-1, b-1))
    E.sort(reverse=1)
    sz = [0]*N
    target_vertices = []
    cnt = 0
    while cnt < T:
        vline = readline()
        if vline.strip() == "":
            continue
        v = int(vline)-1
        target_vertices.append(v)
        cnt += 1
    for v in target_vertices:
        sz[v] = 1
    prt = list(range(N))
    # flatten root and unite
    d = T - K - 1
    idx = 0
    while idx < len(E):
        c, a, b = E[idx]
        # root(a)
        x = a
        while prt[x] != x:
            prt[x] = prt[prt[x]]
            x = prt[x]
        pa = x
        # root(b)
        x = b
        while prt[x] != x:
            prt[x] = prt[prt[x]]
            x = prt[x]
        pb = x
        if sz[pa] == 0 or sz[pb] == 0:
            # unite(a, b)
            if pa < pb:
                prt[pb] = pa
                sz[pa] += sz[pb]
            else:
                prt[pa] = pb
                sz[pb] += sz[pa]
            res -= c
            idx += 1
            continue
        if d > 0:
            d -= 1
            # unite(a, b)
            if pa < pb:
                prt[pb] = pa
                sz[pa] += sz[pb]
            else:
                prt[pa] = pb
                sz[pb] += sz[pa]
            res -= c
        idx += 1
    write("Case %d: %d\n" % (i, res))
    i += 1