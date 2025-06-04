x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

s = abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))
a = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
b = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
c = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
r = s / (a + b + c)

print(max(a, b, c) * r / (2 * r + max(a, b, c)))