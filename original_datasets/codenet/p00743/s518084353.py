import sys
import heapq
if sys.version[0] == '2':
    range, input = xrange, raw_input
MAX_SPEED = 30
while True:
    N, M = map(int, input().split())
    if not (N | M):
        break
    S, G = map(lambda x: int(x) - 1, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(M):
        x, y, d, c = map(int, input().split())
        edge[x - 1].append((y - 1, d, c))
        edge[y - 1].append((x - 1, d, c))
    INF = float('inf')
    dist = [[[INF for _ in range(N)] for _ in range(MAX_SPEED + 1)] for _ in range(N)]
    que = [(0.0, S, 0, S)]
    while que:
        cost, now, v, prev = heapq.heappop(que)
        if cost > dist[now][v][prev]:
            continue
        if now == G and v == 1:
            print("{:.20f}".format(cost))
            break
        dist[now][v][prev] = cost
        for x, d, c in edge[now]:
            if x == prev:
                continue
            if 0 < v <= c and dist[x][v][now] > dist[now][v][prev] + d / v:
                dist[x][v][now] = dist[now][v][prev] + d / v
                heapq.heappush(que, (dist[x][v][now], x, v, now))
            if v < c and dist[x][v + 1][now] > dist[now][v][prev] + d / (v + 1):
                dist[x][v + 1][now] = dist[now][v][prev] + d / (v + 1)
                heapq.heappush(que, (dist[x][v + 1][now], x, v + 1, now))
            if 1 < v <= c + 1 and dist[x][v - 1][now] > dist[now][v][prev] + d / (v - 1):
                dist[x][v - 1][now] = dist[now][v][prev] + d / (v - 1)
                heapq.heappush(que, (dist[x][v - 1][now], x, v - 1, now))
    else:
        print("unreachable")