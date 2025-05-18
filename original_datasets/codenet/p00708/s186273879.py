import heapq
import math

def dist(xyzr0, xyzr1):
    vec = [xyzr0[i] - xyzr1[i] for i in range(3)]
    d = math.sqrt(sum([elem*elem for elem in vec]))
    return max(0, d - xyzr0[3] - xyzr1[3])

def mst(n, dists):
    in_tree = [False] * n
    start = 0
    in_tree[start] = True
    q = [(dists[start][to], start, to) for to in range(n)]
    heapq.heapify(q)
    ans = 0
    cnt = 0
    while q and cnt < n-1:
        dist, fr, to = heapq.heappop(q)
        if in_tree[to]:
            continue
        in_tree[to] = True
        ans += dist
        cnt += 1
        for to_ in range(n):
            heapq.heappush(q, (dists[to][to_], to, to_))
    return ans

def solve(n):
    XYZR = []
    for _ in range(n):
        XYZR.append(list(map(float, input().split())))
    dists = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dists[i][j] = dist(XYZR[i], XYZR[j])
    ans = mst(n, dists)
    print('%.3f' % ans)

while True:
    n = int(input())
    if n == 0:
        break
    solve(n)