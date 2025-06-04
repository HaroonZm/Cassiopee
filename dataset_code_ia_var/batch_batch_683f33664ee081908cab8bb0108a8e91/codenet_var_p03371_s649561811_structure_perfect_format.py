a, b, c, x, y = map(int, input().split())
mx = a if x >= y else b
if c * 2 <= (a + b):
    if c * 2 <= mx:
        print((min(x, y) + abs(x - y)) * c * 2)
    else:
        print(min(x, y) * c * 2 + abs(x - y) * mx)
else:
    print(a * x + b * y)