while True:
    wh = input().split()
    if wh == ['0', '0']:
        break
    w, h = map(int, wh)
    xs, ys = map(int, input().split())
    xg, yg = map(int, input().split())
    n = int(input())
    board = [[0]*w for _ in range(h)]
    colors = [[0]*w for _ in range(h)]
    for _ in range(n):
        c, d, x, y = input().split()
        c = int(c)
        d = int(d)
        x = int(x)
        y = int(y)
        # mark the blocks on board
        if d == 0:
            # horizontal 2x4: width=4 horizontally, height=2 vertically
            for dx in range(4):
                for dy in range(2):
                    colors[y-1+dy][x-1+dx] = c
        else:
            # vertical 2x4: width=2 horizontally, height=4 vertically
            for dx in range(2):
                for dy in range(4):
                    colors[y-1+dy][x-1+dx] = c
    start_color = colors[ys-1][xs-1]
    if start_color == 0:
        print("NG")
        continue
    from collections import deque
    visited = [[False]*w for _ in range(h)]
    q = deque()
    q.append((xs-1, ys-1))
    visited[ys-1][xs-1] = True
    found = False
    while q:
        x, y = q.popleft()
        if x == xg-1 and y == yg-1:
            found = True
            break
        for nx, ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0 <= nx < w and 0 <= ny < h:
                if not visited[ny][nx] and colors[ny][nx] == start_color:
                    visited[ny][nx] = True
                    q.append((nx, ny))
    if found:
        print("OK")
    else:
        print("NG")