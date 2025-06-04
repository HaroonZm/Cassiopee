def is_point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    # Calculate area of the main triangle using cross product
    def area(x1, y1, x2, y2, x3, y3):
        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(px, py, x2, y2, x3, y3)
    A2 = area(x1, y1, px, py, x3, y3)
    A3 = area(x1, y1, x2, y2, px, py)
    # Check if sum of A1, A2 and A3 is same as A
    return A == A1 + A2 + A3

n = int(input())
for _ in range(n):
    xp1, yp1, xp2, yp2, xp3, yp3, xk, yk, xs, ys = map(int, input().split())

    ken_in = is_point_in_triangle(xk, yk, xp1, yp1, xp2, yp2, xp3, yp3)
    ori_in = is_point_in_triangle(xs, ys, xp1, yp1, xp2, yp2, xp3, yp3)

    if (ken_in and not ori_in) or (ori_in and not ken_in):
        print("OK")
    else:
        print("NG")