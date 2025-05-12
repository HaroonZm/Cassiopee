def dfs(dg, gs, ms, used, v):
    if used[v]:
        return dg[gs[v]]
    used[v] = 1
    me = ms[v]
    for i in xrange(len(me)):
        if me[i] in dg:
            ret = dfs(dg, gs, ms, used, gs.index(me[i]))
            for e in ret:
                if e not in dg[gs[v]]:
                    dg[gs[v]].append(e)
        else:
            if me[i] not in dg[gs[v]]:
                dg[gs[v]].append(me[i])
    return dg[gs[v]]

while 1:
    n = input()
    if not n:
        break
    gs = []; ms = []
    dg = {}
    for i in xrange(n):
        g, m = raw_input().split(":")
        gs.append(g); ms.append(m[:-1].split(","))
        dg[g] = []

    dfs(dg, gs, ms, [0]*n, 0)
    print len(dg[gs[0]])