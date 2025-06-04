def solve(nu, mu, du):
    E = []
    vs = [False] * nu
    vs[0] = True
    while True:
        min_dist = float("inf")
        ind = float("inf")
        pf = pt = -1
        for i in xrange(len(du)):
            u, v, w = du[i][0], du[i][1], du[i][2]
            if ((vs[u] and not vs[v]) or (not vs[u] and vs[v])) and min_dist > w:
                min_dist = w
                ind = i
                pf = u
                pt = v
        E.append(min_dist)
        vs[pf] = True
        vs[pt] = True
        du.pop(ind)
        if all(vs):
            break
        i = 0
        while i < len(du):
            u, v = du[i][0], du[i][1]
            if vs[u] and vs[v]:
                du.pop(i)
            else:
                i += 1
    print sum(E) / 100 - len(E)

while True:
    n = input()
    if n == 0:
        exit()
    m = input()
    data = []
    for i in xrange(m):
        data.append(map(int, raw_input().split(",")))
    solve(n, m, data)