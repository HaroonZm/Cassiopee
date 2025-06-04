while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    xs, ys = map(int, input().split())
    xg, yg = map(int, input().split())
    n = int(input())
    board = [[0]*w for _ in range(h)]
    for _ in range(n):
        c, d, x, y = map(int, input().split())
        x -= 1
        y -= 1
        if d == 0:
            # 横方向に長い2x4
            for dx in range(4):
                for dy in range(2):
                    board[y+dy][x+dx] = c
        else:
            # 縦方向に長い4x2
            for dx in range(2):
                for dy in range(4):
                    board[y+dy][x+dx] = c

    start_color = board[ys-1][xs-1]
    if start_color == 0:
        print("NG")
        continue

    visited = [[False]*w for _ in range(h)]
    from collections import deque
    que = deque()
    que.append((ys-1, xs-1))
    visited[ys-1][xs-1] = True
    found = False
    while que:
        y, x = que.popleft()
        if y == yg-1 and x == xg-1:
            found = True
            break
        for dy, dx in [(1,0),(-1,0),(0,1),(0,-1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < h and 0 <= nx < w:
                if not visited[ny][nx] and board[ny][nx] == start_color:
                    visited[ny][nx] = True
                    que.append((ny, nx))
    if found:
        print("OK")
    else:
        print("NG")