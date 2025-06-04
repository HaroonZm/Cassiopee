import math

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = math.hypot(x1 - x2, y1 - y2)
R, r = max(r1, r2), min(r1, r2)

if d > r + R:
    print(4)
elif d == r + R:
    print(3)
elif R - r < d < r + R:
    print(2)
elif d == R - r and d != 0:
    print(1)
else:
    print(0)