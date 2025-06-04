from sys import stdin

for line in stdin:
    a = list(map(float, line.split()))
    x1, y1, x2, y2, x3, y3, x4, y4 = a
    if (
        (x1 < x3 > x2 or x1 > x4 < x2) or
        (y1 < y3 > y2 or y1 > y4 < y2)
    ):
        print('NO')
    else:
        print('YES')