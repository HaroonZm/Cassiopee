a, b, c = map(int, input().split())
if (a + b + c) % 2 == 1:
    x = a * b
    y = b * c
    z = c * a
    t = x if x < y else y
    t = t if t < z else z
    print(t)
else:
    print(0)