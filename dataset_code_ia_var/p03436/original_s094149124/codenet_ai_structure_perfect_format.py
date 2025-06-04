from collections import deque

h, w = map(int, input().split())
S = [input() for _ in range(h)]

que = deque()
que.append((0, 0))
dist = [[-1] * w for _ in range(h)]
dist[0][0] = 1

while que:
    y, x = que.pop()
    for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y + i, x + j
        if 0 <= ny < h and 0 <= nx < w:
            if S[ny][nx] == "#":
                continue
            if dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                que.appendleft((ny, nx))
        if ny == h - 1 and nx == w - 1:
            break

if dist[h - 1][w - 1] == -1:
    ans = -1
else:
    cnt = 0
    for i in range(h):
        cnt += S[i].count(".")
    ans = cnt - dist[h - 1][w - 1]

print(ans)