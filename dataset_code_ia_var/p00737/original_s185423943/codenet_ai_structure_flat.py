mv = [[-1,0],[0,1],[1,0],[0,-1]]
INF = 0x7fffffff
import heapq
while True:
    w, h = map(int, input().split())
    if w == 0:
        break
    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))
    cost = list(map(int, input().split()))
    Q = []
    node = [[[INF for _ in range(4)] for _ in range(w)] for _ in range(h)]
    node[0][0][1] = 0
    heapq.heappush(Q, (0, 0, 0, 1))
    while Q:
        t, r, c, d = heapq.heappop(Q)
        if r == h-1 and c == w-1:
            break
        for i in range(4):
            nd = (d + i) % 4
            nr = r + mv[nd][0]
            nc = c + mv[nd][1]
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            nt = node[r][c][d]
            if arr[r][c] != i:
                nt += cost[i]
            if nt < node[nr][nc][nd]:
                node[nr][nc][nd] = nt
                heapq.heappush(Q, (nt, nr, nc, nd))
    print(node[h-1][w-1][d])