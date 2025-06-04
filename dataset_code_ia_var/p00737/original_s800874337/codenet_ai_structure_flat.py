from collections import defaultdict
import heapq
import sys
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    ss = []
    for _ in range(H):
        ss.append(list(map(int, input().split())))
    cc = list(map(int, input().split()))

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    # Calculer graph (lines)
    lines = defaultdict(set)
    for x in range(W):
        for y in range(H):
            for a in range(4):
                s = (x + y * W) * 4 + a
                costs = cc[:]
                if ss[y][x] <= 3:
                    costs[ss[y][x]] = 0
                for st in range(4):
                    ar = (a + st) % 4
                    tx, ty = x + dx[ar], y + dy[ar]
                    if 0 <= tx < W and 0 <= ty < H:
                        t = (tx + ty * W) * 4 + ar
                        lines[s].add((t, costs[st]))

    N = H * W * 4
    weight = [INF] * N
    s = (0 + 0 * W) * 4 + 1
    weight[s] = 0
    q = [[0, s]]
    heapq.heapify(q)
    while q:
        w, n = heapq.heappop(q)
        for t, ww in lines[n]:
            ww += w
            if weight[t] > ww:
                heapq.heappush(q, [ww, t])
                weight[t] = ww

    min_cost = INF
    for a in range(4):
        val = (W - 1 + (H - 1) * W) * 4 + a
        if min_cost > weight[val]:
            min_cost = weight[val]
    print(min_cost)