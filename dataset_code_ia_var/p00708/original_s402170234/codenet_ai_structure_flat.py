import queue, math
while True:
    n = int(input())
    if n == 0:
        break
    p = [[float(x) for x in input().split()] for _ in range(n)]
    g = [i for i in range(n)]
    q = queue.PriorityQueue()
    cnt_g = n
    ans = 0.0
    # Trouver la racine d'un élément sans fonction
    def root(x):
        if x == g[x]:
            return x
        g[x] = root(g[x])
        return g[x]
    # Construction du graphe
    for i in range(n-1):
        for j in range(i, n):
            dx = p[i][0]-p[j][0]
            dy = p[i][1]-p[j][1]
            dz = p[i][2]-p[j][2]
            d = math.sqrt(dx*dx + dy*dy + dz*dz)
            if d <= p[i][3] + p[j][3]:
                xi = i
                while g[xi] != xi:
                    xi = g[xi]
                xj = j
                while g[xj] != xj:
                    xj = g[xj]
                if xi != xj:
                    g[xi] = xj
                    cnt_g -= 1
            else:
                q.put((d-p[i][3]-p[j][3], i, j))
    # Kruskal excessivement plat sans fonction
    while not q.empty():
        if cnt_g <= 1:
            break
        d, i, j = q.get()
        xi = i
        while g[xi] != xi:
            xi = g[xi]
        xj = j
        while g[xj] != xj:
            xj = g[xj]
        if xi != xj:
            g[xi] = xj
            cnt_g -= 1
            ans += d
    print('{:.3f}'.format(ans))