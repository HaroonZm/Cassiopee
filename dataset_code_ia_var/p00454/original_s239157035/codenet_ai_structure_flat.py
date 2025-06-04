from collections import deque
import sys
input = sys.stdin.readline

while True:
    w_h = input()
    if not w_h:
        continue
    w, h = map(int, w_h.split())
    if w == 0 and h == 0:
        break
    n = int(input())
    x1 = [0]*n
    x2 = [0]*n
    y1 = [0]*n
    y2 = [0]*n
    for i in range(n):
        vals = input().split()
        x1[i] = int(vals[0])
        y1[i] = int(vals[1])
        x2[i] = int(vals[2]) - 1
        y2[i] = int(vals[3]) - 1

    # Start compress for x
    N = n
    xs = set()
    for i in range(N):
        for d in [0, 1]:
            tx1, tx2 = x1[i]-d, x2[i]+d
            if 0 <= tx1 < w:
                xs.add(tx1)
            if 0 <= tx2 < w:
                xs.add(tx2)
    xs = list(xs)
    xs.sort()
    for i in range(N):
        x1[i] = xs.index(x1[i])
        x2[i] = xs.index(x2[i])
    w2 = len(xs)

    # Start compress for y
    ys = set()
    for i in range(N):
        for d in [0, 1]:
            ty1, ty2 = y1[i]-d, y2[i]+d
            if 0 <= ty1 < h:
                ys.add(ty1)
            if 0 <= ty2 < h:
                ys.add(ty2)
    ys = list(ys)
    ys.sort()
    for i in range(N):
        y1[i] = ys.index(y1[i])
        y2[i] = ys.index(y2[i])
    h2 = len(ys)

    board = [[False for _ in range(w2)] for _ in range(h2)]
    for i in range(n):
        for y in range(y1[i], y2[i]+1):
            for x in range(x1[i], x2[i]+1):
                board[y][x] = True

    ans = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for y in range(h2):
        for x in range(w2):
            if board[y][x]:
                continue
            ans += 1
            queue = deque()
            queue.append((x, y))
            board[y][x] = True
            while queue:
                sx, sy = queue.popleft()
                for i in range(4):
                    tx = sx + dx[i]
                    ty = sy + dy[i]
                    if 0 <= tx < w2 and 0 <= ty < h2 and not board[ty][tx]:
                        queue.append((tx, ty))
                        board[ty][tx] = True
    print(ans)