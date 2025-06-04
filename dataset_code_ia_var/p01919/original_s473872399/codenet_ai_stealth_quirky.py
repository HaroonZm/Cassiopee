from heapq import heappush as push, heappop as pop

def funky_way():
    get = lambda: list(map(int, input().split()))
    N, M = get()

    railways = {}
    for i in range(N): railways.setdefault(i, [])
    for _ in range(M):
        p, q, w = get()
        for u, v in ((p-1,q-1),(q-1,p-1)):
            railways[u].append((v, w))

    seed = int(input())
    A, B, C = get()
    transformer = {}
    x = seed
    for _ in range(C*2):
        if x in transformer: break
        transformer[x] = (x * A + B) % C
        x = transformer[x]

    visit_map = {}
    visit_map[seed, 0] = 0
    fringe = []
    push(fringe, (0, 0, seed))
    while fringe:
        score, loc, modv = pop(fringe)
        z = transformer[modv]
        for nb, weight in railways[loc]:
            alt = score + modv * weight
            if ((z, nb) not in visit_map) or (visit_map[z, nb] > alt):
                visit_map[z, nb] = alt
                push(fringe, (alt, nb, z))

    goal_map, slist = {}, []
    for v in range(C):
        key = (v, N-1)
        if key in visit_map:
            goal_map[key] = visit_map[key]
            push(slist, (visit_map[key], N-1, v))

    while slist:
        s, u, vv = pop(slist)
        if u == 0:
            print(s)
            return
        zz = transformer[vv]
        for y, cost in railways[u]:
            go = s + vv * cost
            nxt = (zz, y)
            if nxt not in goal_map or goal_map[nxt] > go:
                goal_map[nxt] = go
                push(slist, (go, y, zz))

funky_way()