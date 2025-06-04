def can_separate(points_black, points_white):
    # Combine points with colors: black=0, white=1
    points = [(x, y, 0) for (x, y) in points_black] + [(x, y, 1) for (x, y) in points_white]

    # If all points are same color or no points, trivially separate
    if not points_black or not points_white:
        return True

    # To check if two sets separated by a line, try all pairs of points to define line directions
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1, c1 = points[i]
            x2, y2, c2 = points[j]
            # Skip if points have same position (problem states they don't)
            # Direction vector orthogonal to line connecting points i and j
            dx = x2 - x1
            dy = y2 - y1

            # The line direction vector can be considered perpendicular to vector (dx, dy)
            # We'll use vector (-dy, dx) for line direction

            # Define the line: ax + by + c = 0 with a=-dy, b=dx
            a = -dy
            b = dx

            # To avoid overflow, no need to normalize because only relative sign matters

            # Compute c so that line doesn't pass through points i or j
            # Since line is infinite, any line parallel and not crossing points i,j is valid
            # Let's check two possible lines, slightly shifting by offset (+1 and -1), but here, we actually
            # want to check separation line that doesn't pass through any point.

            # Instead, we just check sign of each point for line through points i and j
            # But line through i and j passes through those points -> line crossing points (forbidden)
            # So we need to consider lines parallel to the line through i and j
            # Try 2 possible offsets: one offset just above the max projection of points i and j along a,b
            # and one just below min

            # Project all points to line normal vector (a,b)
            projections = [a * x + b * y for (x, y, _) in points]

            # The projections of points i and j are:
            pi = a * x1 + b * y1
            pj = a * x2 + b * y2
            p_min = min(pi, pj)
            p_max = max(pi, pj)

            # Candidate offsets for line to not cross points i,j
            # We can try lines at p = p_min - 0.5 and p = p_max + 0.5 (offset sufficiently small)
            candidate_ps = [p_min - 0.5, p_max + 0.5]

            for p in candidate_ps:
                # For each point get sign relative to line ax + by = p
                # sign = (a*x + b*y) - p
                signs = []
                for (x, y, c) in points:
                    val = a * x + b * y - p
                    # Since points have integer coords and p is offset by 0.5, val != 0 always => no point on line
                    s = 1 if val > 0 else -1
                    signs.append((s, c))

                # Check if signs separate the colors
                # One side has only color 0, other side has only color 1
                # That means the signs must split colors perfectly

                side0_colors = set(c for s, c in signs if s == 1)
                side1_colors = set(c for s, c in signs if s == -1)

                if (side0_colors == {0} and side1_colors == {1}) or (side0_colors == {1} and side1_colors == {0}):
                    return True

    return False


def main():
    while True:
        line = input().strip()
        if line == '':
            continue
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break
        points_black = [tuple(map(int, input().split())) for _ in range(n)]
        points_white = [tuple(map(int, input().split())) for _ in range(m)]
        result = "YES" if can_separate(points_black, points_white) else "NO"
        print(result)


if __name__ == "__main__":
    main()