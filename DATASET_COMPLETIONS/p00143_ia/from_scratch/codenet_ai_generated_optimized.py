def point_in_triangle(px, py, x1, y1, x2, y2, x3, y3):
    # Calculate vectors
    v0x, v0y = x3 - x1, y3 - y1
    v1x, v1y = x2 - x1, y2 - y1
    v2x, v2y = px - x1, py - y1

    # Compute dot products
    dot00 = v0x * v0x + v0y * v0y
    dot01 = v0x * v1x + v0y * v1y
    dot02 = v0x * v2x + v0y * v2y
    dot11 = v1x * v1x + v1y * v1y
    dot12 = v1x * v2x + v1y * v2y

    # Compute barycentric coordinates
    denom = dot00 * dot11 - dot01 * dot01
    if denom == 0:
        return False  # Degenerate triangle
    inv_denom = 1 / denom
    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    # Check if point is inside triangle
    return (u >= 0) and (v >= 0) and (u + v < 1)

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    xp1, yp1, xp2, yp2, xp3, yp3, xk, yk, xs, ys = map(int, input().split())
    k_in = point_in_triangle(xk, yk, xp1, yp1, xp2, yp2, xp3, yp3)
    s_in = point_in_triangle(xs, ys, xp1, yp1, xp2, yp2, xp3, yp3)
    print("OK" if k_in != s_in else "NG")