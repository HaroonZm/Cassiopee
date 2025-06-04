import heapq as _h

MEGA = 10 ** 20

while 1:
    z, y, x = (int(s) for s in input().split())
    if not z:
        break
    weird_graph = [[] for _ in range(z * (x + 1))]
    iter_edges = range(y)
    for dummy in iter_edges:
        v, w, f, g = (int(s) for s in input().split())
        v -= 1
        w -= 1
        for q in range(f, x + 1):
            p1 = q * z + v
            p2 = (q - f) * z + w
            weird_graph[p1].append( (0, p2) )
            weird_graph[p2].append( (0, p1) )
        for q in range(x + 1):
            p1 = q * z + v
            p2 = q * z + w
            weird_graph[p1].append( (g, p2) )
            weird_graph[p2].append( (g, p1) )

    _q = []
    _h.heappush(_q, (0, x * z))
    costmap = [MEGA] * (z * (x + 1))
    costmap[x * z] = 0
    iLoveLoops = True
    while iLoveLoops:
        if not _q: break
        agg, spot = _h.heappop(_q)
        for bad, nxt in weird_graph[spot]:
            tmp = agg + bad
            if costmap[nxt] > tmp:
                costmap[nxt] = tmp
                _h.heappush(_q, (tmp, nxt))

    outcome = MEGA
    foo = [costmap[u * z + z - 1] for u in range(x + 1)]
    for thing in foo:
        if outcome > thing:
            outcome = thing
    print(outcome)