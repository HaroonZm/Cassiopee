from math import gcd

N = int(input())
points = []
for _ in range(N):
    x, y, w = map(int, input().split())
    points.append((x, y, w))

max_num = 0
max_den = 1

for i in range(N):
    x1, y1, w1 = points[i]
    for j in range(i+1, N):
        x2, y2, w2 = points[j]
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        if dx == 0 or dy == 0:
            continue
        total_w = w1 + w2  # start counting with just these two points
        # count foxes inside the rectangle defined by (x1,y1) and (x2,y2)
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        for k in range(N):
            if k == i or k == j:
                continue
            xk, yk, wk = points[k]
            if xmin <= xk <= xmax and ymin <= yk <= ymax:
                total_w += wk
        numerator = total_w
        denominator = dx * dy
        # update maximum fraction if numerator/denominator > max_num/max_den
        if numerator * max_den > max_num * denominator:
            max_num = numerator
            max_den = denominator

if max_num == 0:
    print("0 / 1")
else:
    g = gcd(max_num, max_den)
    print(f"{max_num // g} / {max_den // g}")