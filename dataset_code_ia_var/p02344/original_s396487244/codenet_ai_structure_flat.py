import sys
readline = sys.stdin.buffer.readline

n, q = map(int, readline().split())

par = [i for i in range(n+1)]
rank = [0] * (n+1)
weight = [0] * (n+1)

for _ in range(q):
    s = readline().rstrip().decode('utf-8')
    if s[0] == "0":
        com, a, b, w = map(int, s.split())
    else:
        com, a, b = map(int, s.split())
    if com:
        # same check
        x = a
        xx = []
        while par[x] != x:
            xx.append(x)
            x = par[x]
        rx = x
        for xi in reversed(xx):
            weight[xi] += weight[par[xi]]
            par[xi] = rx
        y = b
        yy = []
        while par[y] != y:
            yy.append(y)
            y = par[y]
        ry = y
        for yi in reversed(yy):
            weight[yi] += weight[par[yi]]
            par[yi] = ry
        if rx == ry:
            print(weight[a] - weight[b])
        else:
            print("?")
    else:
        # union
        x = a
        xx = []
        while par[x] != x:
            xx.append(x)
            x = par[x]
        rx = x
        for xi in reversed(xx):
            weight[xi] += weight[par[xi]]
            par[xi] = rx
        y = b
        yy = []
        while par[y] != y:
            yy.append(y)
            y = par[y]
        ry = y
        for yi in reversed(yy):
            weight[yi] += weight[par[yi]]
            par[yi] = ry
        if rx == ry:
            continue
        if rank[rx] < rank[ry]:
            par[rx] = ry
            weight[rx] = w - weight[a] + weight[b]
        else:
            par[ry] = rx
            weight[ry] = -w - weight[b] + weight[a]
            if rank[rx] == rank[ry]:
                rank[rx] += 1