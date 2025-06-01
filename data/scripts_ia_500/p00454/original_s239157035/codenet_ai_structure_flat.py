from collections import deque
import sys
input = sys.stdin.readline

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    n = int(input())
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        x1.append(a)
        y1.append(b)
        x2.append(c - 1)
        y2.append(d - 1)

    xs = set()
    for i in range(n):
        for d in [0, 1]:
            tx1 = x1[i] - d
            tx2 = x2[i] + d
            if 0 <= tx1 < w:
                xs.add(tx1)
            if 0 <= tx2 < w:
                xs.add(tx2)
    xs = list(xs)
    xs.sort()
    for i in range(n):
        x1[i] = xs.index(x1[i])
        x2[i] = xs.index(x2[i])
    w = len(xs)

    ys = set()
    for i in range(n):
        for d in [0, 1]:
            ty1 = y1[i] - d
            ty2 = y2[i] + d
            if 0 <= ty1 < h:
                ys.add(ty1)
            if 0 <= ty2 < h:
                ys.add(ty2)
    ys = list(ys)
    ys.sort()
    for i in range(n):
        y1[i] = ys.index(y1[i])
        y2[i] = ys.index(y2[i])
    h = len(ys)

    board = [[False]*w for _ in range(h)]
    for i in range(n):
        for y in range(y1[i], y2[i]+1):
            for x in range(x1[i], x2[i]+1):
                board[y][x] = True

    ans = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    for y in range(h):
        for x in range(w):
            if board[y][x]:
                continue
            ans += 1
            queue = deque()
            queue.append((x,y))
            board[y][x] = True
            while queue:
                sx, sy = queue.popleft()
                for i in range(4):
                    tx, ty = sx+dx[i], sy+dy[i]
                    if 0 <= tx < w and 0 <= ty < h:
                        if not board[ty][tx]:
                            queue.append((tx, ty))
                            board[ty][tx] = True
    print(ans)