from collections import deque
import sys
input = sys.stdin.readline

def compress(x1, x2, w):
    N = len(x1)
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
    return len(xs)

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    n = int(input())
    x1 = [0] * n
    x2 = [0] * n
    y1 = [0] * n
    y2 = [0] * n
    for i in range(n):
        x1[i], y1[i], x2[i], y2[i] = map(int, input().split())
        x2[i] -= 1
        y2[i] -= 1
    w = compress(x1, x2, w)
    h = compress(y1, y2, h)

    board = [[False] * w for _ in range(h)]
    for i in range(n):
        for y in range(y1[i], y2[i]+1):
            for x in range(x1[i], x2[i]+1):
                board[y][x] = True

    ans = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for y in range(h):
        for x in range(w):
            if board[y][x]:
                continue
            ans += 1
            queue = deque()
            queue.append((x, y))
            while queue:
                sx, sy = queue.popleft()

                for i in range(4):
                    tx, ty = sx+dx[i], sy+dy[i]
                    if 0 <= tx < w and 0 <= ty < h and not board[ty][tx]:
                        queue.append((tx, ty))
                        board[ty][tx] = True
    print(ans)