w, d, n = map(int, input().split())
measured = {}
for _ in range(n):
    x, y, z = map(int, input().split())
    measured[(x-1, y-1)] = z

INF = 10**9
max_alt = 100
min_alt = -100

# Initialize minimum altitude grid with INF and maximum altitude grid with -INF
min_grid = [[-INF for _ in range(d)] for _ in range(w)]
max_grid = [[INF for _ in range(d)] for _ in range(w)]

# For measured points, min and max are fixed to the measured altitude
for (x, y), z in measured.items():
    min_grid[x][y] = z
    max_grid[x][y] = z

# Use Bellman-Ford-like relaxation to find feasible altitudes ranges
# We iterate at most w*d times to propagate constraints between neighboring cells
for _ in range(w*d):
    updated = False
    for x in range(w):
        for y in range(d):
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < w and 0 <= ny < d:
                    # From cell (x,y) to (nx,ny), altitude difference <=1
                    # So min altitude of (nx,ny) >= min_grid[x][y] - 1
                    if min_grid[nx][ny] < min_grid[x][y] - 1:
                        old = min_grid[nx][ny]
                        min_grid[nx][ny] = min_grid[x][y] - 1
                        if max_grid[nx][ny] < min_grid[nx][ny]:
                            print("No")
                            exit()
                        if old != min_grid[nx][ny]:
                            updated = True
                    # max altitude of (nx,ny) <= max_grid[x][y] + 1
                    if max_grid[nx][ny] > max_grid[x][y] + 1:
                        old = max_grid[nx][ny]
                        max_grid[nx][ny] = max_grid[x][y] + 1
                        if min_grid[nx][ny] > max_grid[nx][ny]:
                            print("No")
                            exit()
                        if old != max_grid[nx][ny]:
                            updated = True
    if not updated:
        break

# After relaxation, check consistency again
for x in range(w):
    for y in range(d):
        if min_grid[x][y] > max_grid[x][y]:
            print("No")
            exit()

# We want the assignment that gives the lowest total altitude
# The minimal altitude of each cell is min_grid[x][y], but must be at least min_alt and at most max_alt
# Adjust them into valid range:
for x in range(w):
    for y in range(d):
        if min_grid[x][y] < min_alt:
            min_grid[x][y] = min_alt
        if max_grid[x][y] > max_alt:
            max_grid[x][y] = max_alt
        if min_grid[x][y] > max_grid[x][y]:
            print("No")
            exit()

# The lowest total altitude is sum of minimal altitudes possible at each cell
total = 0
for x in range(w):
    for y in range(d):
        total += min_grid[x][y]
print(total)