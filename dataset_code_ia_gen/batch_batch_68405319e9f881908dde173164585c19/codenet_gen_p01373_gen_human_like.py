import sys

def side_of_line(x, y, x0, y0, x1, y1):
    return (x - x0) * (y1 - y0) - (y - y0) * (x1 - x0)

def count_one_side(points, x0, y0, x1, y1):
    left = 0
    right = 0
    for (x, y) in points:
        val = side_of_line(x, y, x0, y0, x1, y1)
        if val > 0:
            left += 1
        elif val < 0:
            right += 1
        else:
            # On the line, count as neither side
            pass
    return left, right

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        W, H, N = map(int, line.split())
        if W == 0 and H == 0 and N == 0:
            break
        points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(2*N)]

        count = 0
        total = H * H  # total number of pairs: y0 in [0,H], y1 in [0,H]

        for y0 in range(H+1):
            for y1 in range(H+1):
                x0, x1 = 0, W
                left, right = 0, 0
                left = right = 0
                left = 0
                right = 0

                left_count = 0
                right_count = 0
                on_line = 0

                # For each point, determine side relative to line through (0,y0) and (W,y1)
                lcnt = 0
                rcnt = 0

                # Use side_of_line function
                for (x, y) in points:
                    s = side_of_line(x, y, 0, y0, W, y1)
                    if s > 0:
                        lcnt += 1
                    elif s < 0:
                        rcnt += 1
                    else:
                        # On the line is ambiguous; for problem we consider points on the line do not count
                        pass
                if lcnt == N and rcnt == N:
                    count += 1

        result = count / total
        print(f"{result:.10f}")

if __name__ == "__main__":
    main()