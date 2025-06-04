def solve():
    import sys
    input = sys.stdin.readline

    while True:
        n, m, t, p = map(int, input().split())
        if n == 0 and m == 0 and t == 0 and p == 0:
            break
        folds = [tuple(map(int, input().split())) for _ in range(t)]
        punches = [tuple(map(int, input().split())) for _ in range(p)]

        width, height = n, m

        for dx, dy in punches:
            # For each punch, start with a single point at (dx, dy) with count=1
            points = {(dx, dy): 1}
            w, h = width, height
            # Apply folds in reverse order (simulate unfolding)
            for d_i, c_i in reversed(folds):
                new_points = dict()
                if d_i == 1:
                    # vertical fold at c_i from left fold onto right
                    for (x, y), cnt in points.items():
                        if x >= c_i:
                            # right side stays
                            new_points[(x, y)] = new_points.get((x, y), 0) + cnt
                        else:
                            # left side is mirrored onto right
                            x_mirror = 2*c_i - x - 1
                            new_points[(x, y)] = new_points.get((x, y), 0) + cnt
                            new_points[(x_mirror, y)] = new_points.get((x_mirror, y), 0) + cnt
                    w = c_i * 2
                else:
                    # horizontal fold at c_i from bottom fold onto top
                    for (x, y), cnt in points.items():
                        if y >= c_i:
                            # top side stays
                            new_points[(x, y)] = new_points.get((x, y), 0) + cnt
                        else:
                            # bottom side is mirrored onto top
                            y_mirror = 2*c_i - y - 1
                            new_points[(x, y)] = new_points.get((x, y), 0) + cnt
                            new_points[(x, y_mirror)] = new_points.get((x, y_mirror), 0) + cnt
                    h = c_i * 2
                points = new_points
            # After unfolding all folds, sum counts on all initial paper coordinates
            # sum counts of all points found after unfolding jumps
            total = 0
            for (x, y), cnt in points.items():
                # if inside original paper dimensions add count
                if 0 <= x < n and 0 <= y < m:
                    total += cnt
            print(total)