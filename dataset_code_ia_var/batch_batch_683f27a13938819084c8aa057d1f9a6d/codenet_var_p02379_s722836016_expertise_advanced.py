from math import hypot

x1, y1, x2, y2 = map(float, input().split())
print(f'{hypot(x2 - x1, y2 - y1):.5f}')