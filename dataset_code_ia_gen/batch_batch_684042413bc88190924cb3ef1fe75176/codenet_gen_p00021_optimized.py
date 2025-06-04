import sys

input = sys.stdin.readline
n = int(input())
eps = 1e-9
for _ in range(n):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(float, input().split())
    dx1, dy1 = x2 - x1, y2 - y1
    dx2, dy2 = x4 - x3, y4 - y3
    # Check cross product close to zero
    if abs(dx1*dy2 - dy1*dx2) < eps:
        print("YES")
    else:
        print("NO")