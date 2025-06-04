inf = 100000000

while 1:
    n, m, c, s, g = map(int, raw_input().split())
    if n == 0 and m == 0:
        break

    rosen = []
    for _ in range(c + 1):
        map0 = []
        for __ in range(n + 1):
            map0.append([inf] * (n + 1))
        for i in range(1, n + 1):
            map0[i][i] = 0
        rosen.append(map0)

    for _ in range(m):
        x, y, d, c0 = map(int, raw_input().split())
        rosen[c0][x][y] = min(rosen[c0][x][y], d)
        rosen[c0][y][x] = min(rosen[c0][y][x], d)

    unchin = list(map(int, raw_input().split()))
    unchin.insert(0, 0)
    uth = [[]]
    for __ in range(1, c + 1):
        ddis = list(map(int, raw_input().split()))
        ddis.insert(0, 0)
        dcost = list(map(int, raw_input().split()))
        uth.append([ddis, dcost])

    # Floyd-Warshall for each line
    for l in range(1, c + 1):
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if rosen[l][i][j] > rosen[l][i][k] + rosen[l][k][j]:
                        rosen[l][i][j] = rosen[l][i][k] + rosen[l][k][j]

    bigmap = []
    for __ in range(n + 1):
        bigmap.append([inf] * (n + 1))
    for i in range(1, n + 1):
        bigmap[i][i] = 0

    # Calculation block as flat code
    for l in range(1, c + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis = rosen[l][i][j]
                fare = 0
                if dis >= inf:
                    cost = inf
                elif unchin[l] == 1:
                    cost = uth[l][1][0] * dis
                else:
                    ddis = uth[l][0]
                    dcost = uth[l][1]
                    p = 1
                    while p < unchin[l] and dis > ddis[p]:
                        fare += (ddis[p] - ddis[p - 1]) * dcost[p - 1]
                        p += 1
                    fare += (dis - ddis[p - 1]) * dcost[p - 1]
                    cost = fare
                if bigmap[i][j] > cost:
                    bigmap[i][j] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if bigmap[i][j] > bigmap[i][k] + bigmap[k][j]:
                    bigmap[i][j] = bigmap[i][k] + bigmap[k][j]

    ans = bigmap[s][g]
    if ans < inf:
        print(ans)
    else:
        print(-1)