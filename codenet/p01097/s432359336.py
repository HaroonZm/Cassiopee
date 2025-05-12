from collections import deque
while 1:
    n, k, s = map(int, raw_input().split())
    if n==0:break
    ps = [map(int, raw_input().split()) for i in xrange(n)]

    G = [[] for i in xrange(n)]
    for i in xrange(n):
        xi, yi, zi = ps[i]
        for j in xrange(i+1, n):
            if i==j: continue
            xj, yj, zj = ps[j]

            dx = abs(xi-xj)
            dy = abs(yi-yj)
            dz = abs(zi-zj)

            if dx < s and dy < s and dz < s:
                cost = 2*((s-dx)*(s-dy)+(s-dy)*(s-dz)+(s-dz)*(s-dx))
                G[i].append((j, cost))
                G[j].append((i, cost))
    if k == 1:
        print 6*s*s
        continue

    ans = -1
    leaf = set()
    used = [0]*n
    for i in xrange(n):
        if len(G[i]) == 0:
            used[i] = 1
        elif len(G[i]) == 1:
            leaf.add(i)
    for v in leaf:
        if used[v]:
            continue
        used[v] = 1
        prev = t = None
        deq = deque()
        su = 0
        while 1:
            if prev is not None and len(G[v]) == 1:
                break
            for t, cost in G[v]:
                if t == prev:
                    continue
                used[t] = 1
                if len(deq) < k-1:
                    deq.append(cost)
                    su += cost
                else:
                    su -= deq.popleft()
                    deq.append(cost)
                    su += cost
                break
            if len(deq) == k-1:
                ans = max(ans, su)
            v, prev = t, v
    for v in xrange(n):
        if used[v]:
            continue
        prev = t = None
        used[v] = 1
        u = set([v])
        while v is not None and used[v] < 3:
            for t, cost in G[v]:
                if t == prev:
                    continue
                used[t] += 1
                u.add(t)
                break
            v, prev = t, v
        cont = k if len(u) == k else k-1
        prev = t = None
        deq = deque(); su = 0
        for i in xrange(2*len(u)):
            for t, cost in G[v]:
                if t == prev:
                    continue
                if len(deq) < cont:
                    deq.append(cost)
                    su += cost
                else:
                    su -= deq.popleft()
                    su += cost
                    deq.append(cost)
                break
            if len(deq) == cont:
                ans = max(ans, su)
            v, prev = t, v

    if ans == -1:
        print -1
    else:
        print 6*k*s*s - ans