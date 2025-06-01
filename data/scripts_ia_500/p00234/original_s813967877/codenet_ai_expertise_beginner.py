import heapq

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

while True:
    w, h = map(int, input().split())
    if w == 0:
        break
    f, m, o = map(int, input().split())
    c = []
    for _ in range(h):
        row = list(map(int, input().split()))
        c.append(row)

    d = []
    for _ in range(m + 1):
        layer = []
        for _ in range(h):
            layer.append([float('inf')] * w)
        d.append(layer)

    heap = []
    start_o = o - 1
    for j in range(w):
        start_cost = -min(0, c[0][j])
        d[start_o][0][j] = start_cost
        heapq.heappush(heap, (start_cost, start_o, 0, j))

    while heap:
        cost, ox, i, j = heapq.heappop(heap)

        if d[ox][i][j] < cost or ox <= 1:
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue

            cell = c[ni][nj]

            if cell < 0:
                if ox - 1 >= 0:
                    new_cost = cost - cell
                    if d[ox - 1][ni][nj] > new_cost:
                        d[ox - 1][ni][nj] = new_cost
                        heapq.heappush(heap, (new_cost, ox - 1, ni, nj))
            else:
                nox = ox - 1 + cell
                if nox > m:
                    nox = m
                if d[nox][ni][nj] > cost:
                    d[nox][ni][nj] = cost
                    heapq.heappush(heap, (cost, nox, ni, nj))

    ans = float('inf')
    for j in range(w):
        for ox in range(1, m + 1):
            if d[ox][h - 1][j] < ans:
                ans = d[ox][h - 1][j]

    if ans <= f:
        print(int(ans))
    else:
        print('NA')