import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline()

def get_line_sums(grid, n, start_r, start_c, target_sum, used):
    results = []
    # Try horizontal line (left to right)
    s = 0
    path = []
    for c in range(start_c, n):
        if used[start_r][c]:
            break
        s += grid[start_r][c]
        path.append((start_r, c))
        if s == target_sum:
            results.append(path[:])
            break
        if s > target_sum:
            break
    # Try horizontal line (right to left)
    s = 0
    path = []
    for c in range(start_c, -1, -1):
        if used[start_r][c]:
            break
        s += grid[start_r][c]
        path.append((start_r, c))
        if s == target_sum:
            results.append(path[:])
            break
        if s > target_sum:
            break
    # Try vertical line (top to bottom)
    s = 0
    path = []
    for r in range(start_r, n):
        if used[r][start_c]:
            break
        s += grid[r][start_c]
        path.append((r, start_c))
        if s == target_sum:
            results.append(path[:])
            break
        if s > target_sum:
            break
    # Try vertical line (bottom to top)
    s = 0
    path = []
    for r in range(start_r, -1, -1):
        if used[r][start_c]:
            break
        s += grid[r][start_c]
        path.append((r, start_c))
        if s == target_sum:
            results.append(path[:])
            break
        if s > target_sum:
            break
    return results

def can_place_all_lines(grid, n, start_points, used, idx):
    if idx == len(start_points):
        # Check all cells are used
        for r in range(n):
            for c in range(n):
                if not used[r][c]:
                    return False
        return True

    r, c = start_points[idx]
    target_sum = -grid[r][c]

    # Get all candidate line paths for this start point
    candidates = get_line_sums(grid, n, r, c, target_sum, used)
    # For each candidate, try placing it and proceed
    for path in candidates:
        # Check if path passes through other start points
        start_points_count = 0
        for rr, cc in path:
            if grid[rr][cc] < 0:
                start_points_count += 1
        if start_points_count > 1:
            continue

        # Mark path as used
        for rr, cc in path:
            used[rr][cc] = True
        used[r][c] = True  # origin always used (included in path but ensure)
        if can_place_all_lines(grid, n, start_points, used, idx + 1):
            return True
        # Backtrack
        for rr, cc in path:
            used[rr][cc] = False

    return False

def main():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        grid = []
        for _ in range(n):
            grid.append(list(map(int, sys.stdin.readline().split())))
        # find start points
        start_points = []
        for r in range(n):
            for c in range(n):
                if grid[r][c] < 0:
                    start_points.append((r, c))
        used = [[False]*n for _ in range(n)]
        # For used, initially mark start points as not used, 
        # as lines must pass start points (line includes start point cell)
        # but until set, just False
        # Actually start points must be included by line segments, so mark after line found

        # Because order affects backtracking, we sort start points to optimize:
        # Try points with fewer candidates first
        def count_candidates(sp):
            r, c = sp
            return len(get_line_sums(grid, n, r, c, -grid[r][c], used))
        # But this uses used state that is empty and common for all, so ignore

        # We just proceed as read order

        # Attempt to find solution
        ans = can_place_all_lines(grid, n, start_points, used, 0)
        print("YES" if ans else "NO")

if __name__ == "__main__":
    main()