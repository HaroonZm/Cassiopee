from sys import stdin

def rects_overlap(a, b, c, d):
    return a <= d and c <= b

def lines():
    for line in stdin:
        yield tuple(map(float, line.split()))

for ax, ay, bx, by, cx, cy, dx, dy in lines():
    print('YES' if rects_overlap(ax, bx, cx, dx) and rects_overlap(ay, by, cy, dy) else 'NO')