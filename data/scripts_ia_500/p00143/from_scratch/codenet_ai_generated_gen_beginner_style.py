def is_point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    # 使用重心座標法判斷點是否在三角形內部
    # 計算面積
    def area(x1, y1, x2, y2, x3, y3):
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))
    A = area(x1, y1, x2, y2, x3, y3)
    A1 = area(px, py, x2, y2, x3, y3)
    A2 = area(x1, y1, px, py, x3, y3)
    A3 = area(x1, y1, x2, y2, px, py)
    return A == A1 + A2 + A3 and A != 0

n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))
    x1, y1, x2, y2, x3, y3, xk, yk, xs, ys = data
    k_in = is_point_in_triangle(xk, yk, x1, y1, x2, y2, x3, y3)
    s_in = is_point_in_triangle(xs, ys, x1, y1, x2, y2, x3, y3)
    if k_in != s_in:
        print("OK")
    else:
        print("NG")