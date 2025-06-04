from collections import deque

def main():
    """
    Main function to determine either the finite area of a region or output 'INF' if the region is unbounded.
    The input describes a set of horizontal and vertical line segments forming a grid, and the task is to 
    compute the area of the outside (unbounded) region accessible from the origin (0, 0).
    """
    # Read grid dimensions: n horizontal segments, m vertical segments
    n, m = map(int, input().split())

    INF = 10**20  # Representation of infinity for map limits

    # Sets to collect unique x and y coordinates encountered, including bounds
    mapX = {INF, -INF}
    mapY = {INF, -INF}

    # Movement arrays, representing directions: left, up, right, down
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # Arrays to store input horizontal (lh) and vertical (lv) segments
    lh = [None] * n
    lv = [None] * m

    # Parse horizontal lines; collect x-ranges and their y
    for i in range(n):
        a, b, c = map(int, input().split())  # From x=a to x=b at y=c
        mapX.add(a)
        mapX.add(b)
        mapY.add(c)
        lh[i] = [a, b, c]

    # Parse vertical lines; collect y-ranges and their x
    for i in range(m):
        d, e, f = map(int, input().split())  # At x=d from y=e to y=f
        mapX.add(d)
        mapY.add(e)
        mapY.add(f)
        lv[i] = [d, e, f]

    # Discretize all x, y coordinates
    x_len = len(mapX)*2 - 1  # Space for real coordinates and gaps between
    y_len = len(mapY)*2 - 1

    mapX, mapY = sorted(list(mapX)), sorted(list(mapY))  # Order all coordinates

    # Build mappings: coordinate value -> compressed index
    mapXi = {val: i for i, val in enumerate(mapX)}
    mapYi = {val: i for i, val in enumerate(mapY)}

    # Create grid (initially empty) to mark walls and regions
    grid = [[0] * y_len for _ in range(x_len)]

    # Arrays for distances between x/y lines (used for area computation)
    x_range = [0] * x_len
    y_range = [0] * y_len

    # Mark boundaries as infinitely wide/tall to catch unbounded region
    x_range[0] = x_range[-1] = INF
    y_range[0] = y_range[-1] = INF

    # Find the start position (mapped index for (0, 0)), and compute cell dimensions
    sx = sy = None  # Starting cell (will contain 0,0)
    for i, (x1, x2) in enumerate(zip(mapX, mapX[1:])):
        x_range[i * 2 + 1] = x2 - x1        # Gap width
        if x1 <= 0 <= x2:
            sx = i * 2 + 1                  # x cell containing 0

    for i, (y1, y2) in enumerate(zip(mapY, mapY[1:])):
        y_range[i * 2 + 1] = y2 - y1        # Gap height
        if y1 <= 0 <= y2:
            sy = i * 2 + 1                  # y cell containing 0

    # Mark horizontal walls in grid
    for a, b, c in lh:
        y = mapYi[c] * 2                   # Wall at y coordinate, between x coords
        for x in range(mapXi[a] * 2 + 1, mapXi[b] * 2 + 1, 2):  # Walls exist on lines
            grid[x][y] = 1                 # Mark wall cell

    # Mark vertical walls in grid
    for a, b, c in lv:
        x = mapXi[a] * 2                   # Wall at x coordinate, between y coords
        for y in range(mapYi[b] * 2 + 1, mapYi[c] * 2 + 1, 2):  # Walls exist on lines
            grid[x][y] = 1                 # Mark wall cell

    # Begin BFS from the cell containing the origin (0, 0)
    q = deque()
    grid[sx][sy] = 1                       # Mark as visited
    q.appendleft([sx, sy])

    ans = x_range[sx] * y_range[sy]        # Initial area (for the origin cell)

    # Breadth-first traversal to accumulate area of the connected region
    while q:
        x, y = q.pop()

        # Explore four directions
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]          # Step to wall
            if grid[nx][ny]:                       # Check if hit wall or visited
                continue
            nx += dx[i]
            ny += dy[i]                            # Go past wall into cell
            if grid[nx][ny]:                       # Already visited
                continue

            grid[nx][ny] = 1                       # Mark as visited
            q.appendleft([nx, ny])                 # Add to exploration queue
            ans += x_range[nx] * y_range[ny]       # Add area of this cell

            # If area reaches 'infinite', report unbounded region
            if ans >= INF:
                print("INF")
                return

    # Output the total computed (finite) area
    print(ans)


if __name__ == "__main__":
    main()