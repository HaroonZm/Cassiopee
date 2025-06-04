import sys
import math

def segment_circle_intersect(px, py, qx, qy, cx, cy, r):
    # Translate coordinates for simplicity
    px -= cx
    py -= cy
    qx -= cx
    qy -= cy

    dx = qx - px
    dy = qy - py
    a = dx*dx + dy*dy
    b = 2*(px*dx + py*dy)
    c = px*px + py*py - r*r

    disc = b*b - 4*a*c
    if disc < 0:
        return False

    sqrt_disc = math.sqrt(disc)
    t1 = (-b - sqrt_disc) / (2*a)
    t2 = (-b + sqrt_disc) / (2*a)

    # Check if intersection point lies on segment
    return (0 < t1 < 1) or (0 < t2 < 1)

input = sys.stdin.readline

while True:
    n = input()
    if not n:
        break
    n = int(n)
    if n == 0:
        break
    walls = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    for _ in range(m):
        tx, ty, sx, sy = map(int, input().split())
        visible = True
        for (wx, wy, r) in walls:
            if segment_circle_intersect(sx, sy, tx, ty, wx, wy, r):
                visible = False
                break
        print("Danger" if visible else "Safe")