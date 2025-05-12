from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    W, H = map(int, readline().split())
    S = [readline().strip() for i in range(H)]
    R = [[0]*W for i in range(H)]
    P = []
    cnt = 0
    for i in range(H):
        Si = S[i]
        for j in range(W):
            if Si[j] == 's':
                sx = j; sy = i
                R[i][j] = 1
                cnt += 1
            elif Si[j] == 'g':
                gx = j; gy = i
            elif Si[j] == '*':
                P.append((j, i))
            elif Si[j] == '.':
                cnt += 1
                R[i][j] = 1
    dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
    INF = 10**18

    dist1 = [[INF]*W for i in range(H)]
    que = deque(P)
    for x, y in P:
        dist1[y][x] = 0
    while que:
        x, y = que.popleft()
        c = dist1[y][x]+1
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if S[ny][nx] in '*#' or dist1[ny][nx] != INF:
                continue
            dist1[ny][nx] = c
            que.append((nx, ny))

    dist2 = [[INF]*W for i in range(H)]
    que = deque([(gx, gy)])
    dist2[gy][gx] = 0
    while que:
        x, y = que.popleft()
        c = dist2[y][x]+1
        for dx, dy in dd:
            nx = x + dx; ny = y + dy
            if S[ny][nx] in '*#' or dist2[ny][nx] != INF:
                continue
            dist2[ny][nx] = c
            que.append((nx, ny))

    left = 0; right = 10**21
    BASE = 10**9
    for i in range(71):
        mid = (left + right) // 2
        su = 0
        for i in range(H):
            for j in range(W):
                if not R[i][j]:
                    continue
                su += min(dist1[i][j]*BASE + mid, dist2[i][j]*BASE)
        if mid*cnt > su:
            right = mid
        else:
            left = mid
    write("%.16f\n" % min(dist1[sy][sx] + left / BASE, dist2[sy][sx]))
solve()