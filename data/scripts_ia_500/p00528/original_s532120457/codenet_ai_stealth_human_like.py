from heapq import heappush, heappop

M, N, K = map(int, input().split())

rows = [[] for _ in range(M)]
cols = [[] for _ in range(N)]

for idx in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    rows[x].append((y, idx))
    cols[y].append((x, idx))

graph_row = [[] for _ in range(K)]
graph_col = [[] for _ in range(K)]

for r in range(M):
    points = rows[r]
    if points:
        points.sort()
        prev = points[0]
        for curr in points[1:]:
            dist = curr[0] - prev[0]
            graph_row[prev[1]].append((curr[1], dist))
            graph_row[curr[1]].append((prev[1], dist))
            prev = curr

for c in range(N):
    points = cols[c]
    if points:
        points.sort()
        prev = points[0]
        for curr in points[1:]:
            dist = curr[0] - prev[0]
            graph_col[prev[1]].append((curr[1], dist))
            graph_col[curr[1]].append((prev[1], dist))
            prev = curr

INF = 10 ** 18
dist0 = [INF] * K
dist1 = [INF] * K

heap = []
if rows[0]:
    first_y, first_idx = rows[0][0]
    # starting from first point in first row
    heappush(heap, (first_y, 0, first_idx))

while heap:
    cost, t, v = heappop(heap)
    if t == 0:
        if dist0[v] < cost:
            continue
        for w, d in graph_row[v]:
            if cost + d < dist0[w]:
                dist0[w] = cost + d
                heappush(heap, (dist0[w], 0, w))
        if cost + 1 < dist1[v]:
            dist1[v] = cost + 1
            heappush(heap, (cost + 1, 1, v))
    else:
        if dist1[v] < cost:
            continue
        for w, d in graph_col[v]:
            if cost + d < dist1[w]:
                dist1[w] = cost + d
                heappush(heap, (dist1[w], 1, w))
        if cost + 1 < dist0[v]:
            dist0[v] = cost + 1
            heappush(heap, (cost + 1, 0, v))

answer = INF

if rows[M-1]:
    last_y, idx = rows[M-1][-1]
    answer = min(answer, dist0[idx] + (N - 1 - last_y))
if cols[N-1]:
    last_x, idx = cols[N-1][-1]
    answer = min(answer, dist1[idx] + (M - 1 - last_x))

if answer == INF:
    print(-1)
else:
    print(answer)