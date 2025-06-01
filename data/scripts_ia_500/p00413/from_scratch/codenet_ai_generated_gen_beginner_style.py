x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

area1 = w1 * h1
area2 = w2 * h2

overlap_w = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
overlap_h = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))

overlap_area = overlap_w * overlap_h

result = area1 + area2 - 2 * overlap_area

print(result)