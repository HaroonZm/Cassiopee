w, h, n = map(int, input().split())

dist = []
for _ in range(n):
    x, y = map(int, input().split())
    dist.append([x, y])

start = dist.pop(0)
x1, y1 = start

cnt = 0
for d in dist:
    x2, y2 = d
    while 1:
        if x1 == x2 and y1 == y2:
            break

        cnt += 1
        if x1 < x2 and y1 < y2:
            x1 += 1
            y1 += 1
        elif x1 == x2 and y1 < y2:
            y1 += 1
        elif x1 > x2 and y1 < y2:
            if y1 != h:
                y1 += 1
            else:
                x1 -= 1
        elif x1 < x2 and y1 == y2:
            x1 += 1
        elif x1 > x2 and y1 == y2:
            x1 -= 1
        elif x1 < x2 and y1 > y2:
            if y1 != 0:
                y1 -= 1
            else:
                x1 += 1
        elif x1 == x2 and y1 > y2:
            y1 -= 1
        elif x1 > x2 and y1 > y2:
            x1 -= 1
            y1 -= 1

print(cnt)