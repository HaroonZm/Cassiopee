x1, y1, x2, y2 = map(int, input().split())
a = x2 + y1 - y2
b = y2 - x1 + x2
c = x1 - x2 + x2 + y1 - y2
d = y1 - y2 + y2 - x1 + x2
print(a, b, c, d)