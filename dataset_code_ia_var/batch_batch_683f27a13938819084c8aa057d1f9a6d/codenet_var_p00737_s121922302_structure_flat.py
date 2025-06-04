import heapq

w, h = 0, 0
grid = []
c = []
inf = 1000000007
y = [0, 1, 0, -1]
x = [1, 0, -1, 0]

while True:
    w, h = map(int, input().split())
    if w == 0:
        break

    grid = []
    for _ in range(h):
        grid.append(list(map(int, input().split())))
    c = list(map(int, input().split()))

    d = [[[inf] * 4 for _ in range(w)] for _ in range(h)]
    d[0][0][0] = 0
    pq = [[0, 0, 0, 0]]
    heapq.heapify(pq)
    res = inf

    while pq:
        ccost, cy, cx, cd = heapq.heappop(pq)
        if d[cy][cx][cd] < ccost:
            continue
        if cy == h - 1 and cx == w - 1:
            res = ccost
            break
        for i in range(4):
            nd = (cd + i) % 4
            ny = cy + y[nd]
            nx = cx + x[nd]
            if not (0 <= ny < h and 0 <= nx < w):
                continue
            if i == grid[cy][cx]:
                ncost = ccost
            else:
                ncost = ccost + c[i]
            if ncost < d[ny][nx][nd]:
                d[ny][nx][nd] = ncost
                heapq.heappush(pq, [ncost, ny, nx, nd])

    print(res)