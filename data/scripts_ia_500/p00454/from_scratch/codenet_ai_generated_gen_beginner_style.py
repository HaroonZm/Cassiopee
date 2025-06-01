def main():
    import sys
    sys.setrecursionlimit(10**7)

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        w, h = map(int, line.split())
        if w == 0 and h == 0:
            break
        n = int(sys.stdin.readline())

        vertical_cuts = set()
        horizontal_cuts = set()
        vertical_cuts.add(0)
        vertical_cuts.add(w)
        horizontal_cuts.add(0)
        horizontal_cuts.add(h)

        tapes = []
        for _ in range(n):
            x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
            tapes.append((x1, y1, x2, y2))
            vertical_cuts.add(x1)
            vertical_cuts.add(x2)
            horizontal_cuts.add(y1)
            horizontal_cuts.add(y2)

        vertical_cuts = sorted(vertical_cuts)
        horizontal_cuts = sorted(horizontal_cuts)

        # Create look-up index for each coordinate
        x_index = {}
        for i, x in enumerate(vertical_cuts):
            x_index[x] = i
        y_index = {}
        for i, y in enumerate(horizontal_cuts):
            y_index[y] = i

        w_cells = len(vertical_cuts) - 1
        h_cells = len(horizontal_cuts) - 1

        grid = [[0]*h_cells for _ in range(w_cells)]

        # mark masked area
        for x1, y1, x2, y2 in tapes:
            xi1 = x_index[x1]
            xi2 = x_index[x2]
            yi1 = y_index[y1]
            yi2 = y_index[y2]
            for xi in range(xi1, xi2):
                for yi in range(yi1, yi2):
                    grid[xi][yi] = 1  # masked

        visited = [[False]*h_cells for _ in range(w_cells)]

        def neighbors(x,y):
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < w_cells and 0 <= ny < h_cells:
                    yield nx, ny

        def dfs(sx, sy):
            stack = [(sx, sy)]
            visited[sx][sy] = True
            while stack:
                x, y = stack.pop()
                for nx, ny in neighbors(x,y):
                    if not visited[nx][ny] and grid[nx][ny] == 0:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

        count = 0
        for i in range(w_cells):
            for j in range(h_cells):
                if grid[i][j] == 0 and not visited[i][j]:
                    dfs(i, j)
                    count += 1

        print(count)

if __name__ == '__main__':
    main()