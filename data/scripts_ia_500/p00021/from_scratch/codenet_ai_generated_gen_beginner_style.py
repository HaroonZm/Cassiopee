n = int(input())
for _ in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())

    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = x4 - x3
    dy2 = y4 - y3

    # Check for parallelism: cross product of direction vectors should be 0
    # Because of floating point, use a small epsilon
    epsilon = 1e-9
    cross = dx1 * dy2 - dy1 * dx2
    if abs(cross) < epsilon:
        print("YES")
    else:
        print("NO")