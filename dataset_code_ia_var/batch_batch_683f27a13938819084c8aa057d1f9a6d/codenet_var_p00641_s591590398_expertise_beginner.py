while True:
    n = int(input())
    if n == 0:
        break

    g = []
    for i in range(n):
        g.append([])

    for i in range(n):
        parts = input().split()
        v1 = int(parts[0])
        w1 = int(parts[1])
        v2 = int(parts[2])
        w2 = int(parts[3])

        g[i].append((v1, w1))
        g[i].append((v2, w2))

    vis = []
    for i in range(n):
        vis.append(False)

    res = 1

    for i in range(n):
        if vis[i]:
            continue
        ws = []
        p = -1
        u = i
        while True:
            vis[u] = True
            found = False
            for v, w in g[u]:
                if v != p:
                    ws.append(w)
                    p = u
                    u = v
                    found = True
                    break
            if not found or u == i:
                break
        if len(ws) > 0:
            m = max(ws)
            count = 0
            for x in ws:
                if x == m:
                    count += 1
            res = (res * count) % 10007
    print(res)