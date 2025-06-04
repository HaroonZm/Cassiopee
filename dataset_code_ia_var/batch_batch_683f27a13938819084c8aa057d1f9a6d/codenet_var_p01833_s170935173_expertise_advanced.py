import sys
from collections import deque
from functools import partial
from operator import attrgetter

readline = sys.stdin.readline
write = sys.stdout.write

INF = 10 ** 9

def bfs(N, G, s):
    dist = [INF] * N
    label = list(range(N))
    dist[s] = 0
    que = deque([s])
    while que:
        v = que.popleft()
        dv = dist[v] + 1
        lv = label[v]
        for w in G[v]:
            if dist[w] == INF:
                dist[w] = dv
                label[w] = min(lv, label[w])
                que.append(w)
            elif dist[w] == dv:
                label[w] = min(lv, label[w])
    return dist, label

def solve():
    N, A, B, C = map(int, readline().split())
    curr_label = list(range(N))
    LA = list(map(lambda x: int(x) - 1, readline().split()))
    ga = min(LA)
    for i in LA: curr_label[i] = ga
    LB = list(map(lambda x: int(x) - 1, readline().split()))
    gb = min(LB)
    for i in LB: curr_label[i] = gb
    LC = list(map(lambda x: int(x) - 1, readline().split()))
    gc = min(LC)
    for i in LC: curr_label[i] = gc

    G = [set() for _ in range(N)]
    for _ in range(int(readline())):
        x, y = map(int, readline().split())
        lx, ly = curr_label[x - 1], curr_label[y - 1]
        G[lx].add(ly)
        G[ly].add(lx)

    dists = [bfs(N, G, s) for s in (ga, gb, gc)]
    ans, idx = INF, -1
    for i in range(N):
        d = sum(dist[i] for dist, _ in dists)
        if d <= ans:
            l = min(lab[i] for _, lab in dists)
            if d < ans:
                ans, idx = d, l
            else:
                idx = min(idx, l)
    write(f"{ans} {idx+1}\n")

if __name__ == "__main__":
    solve()