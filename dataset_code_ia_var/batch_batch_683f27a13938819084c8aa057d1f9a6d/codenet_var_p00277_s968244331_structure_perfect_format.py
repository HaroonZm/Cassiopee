import sys

f = sys.stdin

n, r, l = map(int, f.readline().split())

appearance = [0] * n
point = [0] * n

top = 0
pre_t = 0

for line in f:
    d, t, x = map(int, line.split())
    d -= 1

    appearance[top] += t - pre_t
    pre_t = t

    point[d] += x

    if x > 0 and top != d:
        if point[top] < point[d]:
            top = d
        elif point[top] == point[d] and d < top:
            top = d
    elif x < 0 and top == d:
        top = point.index(max(point))

appearance[top] += l - pre_t

print(1 + appearance.index(max(appearance)))