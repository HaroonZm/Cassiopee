import heapq
import math

while True:
    n = int(input())
    if n == 0:
        break
    XYZR = []
    for _ in range(n):
        XYZR.append(list(map(float, input().split())))
    dists = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            vec = [XYZR[i][k] - XYZR[j][k] for k in range(3)]
            d = math.sqrt(sum([elem*elem for elem in vec]))
            dists[i][j] = max(0, d - XYZR[i][3] - XYZR[j][3])
    in_tree = [False] * n
    start = 0
    in_tree[start] = True
    q = [(dists[start][to], start, to) for to in range(n)]
    heapq.heapify(q)
    ans = 0
    cnt = 0
    while q and cnt < n-1:
        dist_val, fr, to = heapq.heappop(q)
        if in_tree[to]:
            continue
        in_tree[to] = True
        ans += dist_val
        cnt += 1
        for to_ in range(n):
            heapq.heappush(q, (dists[to][to_], to, to_))
    print('%.3f' % ans)