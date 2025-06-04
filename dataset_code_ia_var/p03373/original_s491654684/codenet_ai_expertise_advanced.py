from operator import itemgetter

a, b, c, x, y = map(int, input().split())

(x, y), (a, b) = sorted(((x, y), (a, b)), key=itemgetter(0), reverse=True)

c2 = 2 * c
res = min(
    a * x + b * y,
    c2 * y + a * (x - y),
    c2 * x,
)

print(res)