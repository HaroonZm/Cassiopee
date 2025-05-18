def make_routes(ns,used, cur):
    if all(used[cur]):
        yield []
    else:
        for i in (d for d,s in zip(range(ns+1), used[cur]) if not s):
            used[cur][i] = used[i][cur] = True
            for ret in make_routes(ns,used,i):
                yield [[cur, i]] + ret
            used[cur][i] = used[i][cur] = False

while True:
    ns,nl = map(int, raw_input().split())
    if ns == 0 and nl == 0:
        break
    costs = [[0]*(ns+1) for _ in xrange(ns+1)]
    used = [[True]*(ns+1) for _ in xrange(ns+1)]
    for _ in xrange(nl):
        a, b, c = map(int, raw_input().split())
        costs[a][b] = costs[b][a] = c
        used[a][b] = used[b][a] = False
    ans = [0,[]]
    for i in xrange(1,ns): #not ns+1
        for route in make_routes(ns, used, i):
            cost = sum(costs[a][b] for a,b in route)
            if ans[0] < cost:
                ans[0] = cost
                ans[1] = route
    print ans[0]
    print "{} {}".format(str(ans[1][0][0])," ".join(str(a[1])for a in ans[1]))