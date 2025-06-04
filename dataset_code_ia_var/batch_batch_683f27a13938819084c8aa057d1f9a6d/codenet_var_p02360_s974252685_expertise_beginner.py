n = int(input())
ys = [0] * 1001
rects = []

for _ in range(n):
    x1y1x2y2 = input().split()
    x1 = int(x1y1x2y2[0])
    y1 = int(x1y1x2y2[1])
    x2 = int(x1y1x2y2[2])
    y2 = int(x1y1x2y2[3])
    rects.append((x2, -1, y1, y2))
    rects.append((x1, 1, y1, y2))

rects.sort(key=lambda r: r[0])

def cumulate(a):
    res = []
    s = 0
    for v in a:
        s += v
        res.append(s)
    return res

max_overlap = 0

for rect in rects:
    x, typ, y1, y2 = rect
    if typ == 1:
        ys[y1] += 1
        ys[y2] -= 1
    else:
        acc = cumulate(ys)
        overlap = max(acc)
        if overlap > max_overlap:
            max_overlap = overlap
        ys[y1] -= 1
        ys[y2] += 1

print(max_overlap)