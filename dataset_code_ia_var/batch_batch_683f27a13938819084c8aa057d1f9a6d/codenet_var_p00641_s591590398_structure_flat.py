while True:
    n = int(input())
    if n == 0:
        break
    g = []
    i = 0
    while i < n:
        temp = input().split()
        v1 = int(temp[0])
        w1 = int(temp[1])
        v2 = int(temp[2])
        w2 = int(temp[3])
        g.append([(v1, w1), (v2, w2)])
        i += 1
    res = 1
    vis = []
    i = 0
    while i < n:
        vis.append(False)
        i += 1
    i = 0
    while i < n:
        if vis[i]:
            i += 1
            continue
        ws = []
        p = -1
        u = i
        while True:
            vis[u] = True
            found = False
            j = 0
            while j < 2:
                v, w = g[u][j]
                if v != p:
                    ws.append(w)
                    p = u
                    u = v
                    found = True
                    break
                j += 1
            if u == i:
                break
        maxw = -1
        k = 0
        while k < len(ws):
            if ws[k] > maxw:
                maxw = ws[k]
            k += 1
        cnt = 0
        k = 0
        while k < len(ws):
            if ws[k] == maxw:
                cnt += 1
            k += 1
        res = (res * cnt) % 10007
        i += 1
    print(res)