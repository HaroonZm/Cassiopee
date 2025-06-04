from operator import itemgetter

a, b, c, x, y = map(int, input().split())

x, y, a, b = max(x, y), min(x, y), max(a, b), min(a, b)

res = min(
    a * x + b * y,
    c * 2 * y + (x - y) * a,
    c * 2 * x
)

print(res)