from sys import stdin
from collections import defaultdict

def readints():
    return map(int, stdin.readline().split())

w, h, n = readints()
segments = [tuple(readints()) for _ in range(n)]

endpoints = [
    (x, y, idx)
    for idx, (x1, y1, x2, y2) in enumerate(segments)
    for (x, y) in [(x1, y1), (x2, y2)]
    if (x in (0, w) or y in (0, h))
]
# Calculate position along the rectangle perimeter
def perimeter_pos(x, y):
    if y == 0: return x
    elif x == w: return w + y
    elif y == h: return w + h + (w - x)
    else: return 2 * w + h + (h - y)

# Only take points on the border (excluding corners if needed)
border_points = [
    (perimeter_pos(x, y), idx)
    for (x, y, idx) in endpoints
    if (x in (0, w) and 0 <= y <= h) or (y in (0, h) and 0 <= x <= w)
]
border_points = sorted(border_points)
edge = [idx for _, idx in border_points]

seen = {}
stack = []
for v in edge:
    if v not in seen:
        stack.append(v)
        seen[v] = len(stack)
    else:
        if seen[v] != len(stack):
            print("NO")
            break
        stack.pop()
else:
    print("YES")