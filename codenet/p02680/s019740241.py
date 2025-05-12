from collections import deque

def main():
    n, m = map(int, input().split())
    INF = 10**20
    mapX = {INF, -INF}
    mapY = {INF, -INF}
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    lh = [None]*n
    lv = [None]*m
    for i in range(n):
        a, b, c = map(int, input().split())
        mapX.add(a)
        mapX.add(b)
        mapY.add(c)
        lh[i] = [a, b, c]
    for i in range(m):
        d, e, f = map(int, input().split())
        mapX.add(d)
        mapY.add(e)
        mapY.add(f)
        lv[i] = [d, e, f]
        
    x_len = len(mapX)*2 - 1
    y_len = len(mapY)*2 - 1
    mapX, mapY = sorted(list(mapX)), sorted(list(mapY))
    mapXi, mapYi = {val:i for i, val in enumerate(mapX)}, {val:i for i, val in enumerate(mapY)}
    grid = [[0]*y_len for _ in range(x_len)]
    
    x_range = [0] * x_len
    y_range = [0] * y_len
    x_range[0] = x_range[-1] = INF
    y_range[0] = y_range[-1] = INF
    
    for i, (x1, x2) in enumerate(zip(mapX, mapX[1:])):
        x_range[i*2 + 1] = x2 - x1
        if x1 <= 0 <= x2:
            sx = i*2 + 1
    
    for i, (y1, y2) in enumerate(zip(mapY, mapY[1:])):
        y_range[i*2 + 1] = y2 - y1
        if y1 <= 0 <= y2:
            sy = i*2 + 1
    
    for a, b, c in lh:
        y = mapYi[c]*2
        for x in range(mapXi[a]*2+1, mapXi[b]*2+1, 2):
            grid[x][y] = 1
    for a, b, c in lv:
        x = mapXi[a]*2
        for y in range(mapYi[b]*2+1, mapYi[c]*2+1, 2):
            grid[x][y] = 1
    q = deque()
    grid[sx][sy] = 1
    q.appendleft([sx, sy])
    ans = x_range[sx] * y_range[sy]
    while q:
        x, y = q.pop()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if grid[nx][ny]:
                continue
            nx += dx[i]
            ny += dy[i]
            if grid[nx][ny]:
                continue
            grid[nx][ny] = 1
            q.appendleft([nx, ny])
            ans += x_range[nx]*y_range[ny]
            if ans >= INF:
                print("INF")
                return
    print(ans)
        
            
if __name__ == "__main__":
    main()