w, h, n = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(n)]
x1, y1 = dist.pop(0)
cnt = 0
for x2, y2 in dist:
    while (x1, y1) != (x2, y2):
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