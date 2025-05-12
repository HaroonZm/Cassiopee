a, b, c, x, y = map(int, input().split())
p1 = a * x + b * y
p2 = 2 * c * (min(x, y))
p3 = 2 * c * (max(x, y))
if x > y:
    p2 += a * (x - y)
elif x < y:
    p2 += b * (y - x)

print(min(p1, p2, p3))