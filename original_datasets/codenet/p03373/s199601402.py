a, b, c, x, y = map(int, input().split())

if x < y:
    a, b = b, a
    x, y = y, x

case1 = a * x + b * y
case2 = c * 2 * y + (x - y) * a
case3 = c * 2 * x

print(min(case1, case2, case3))