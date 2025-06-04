import math

a, b, x = map(int, input().split())

vol = a ** 2 * b
ans = 0

if vol / 2 < x:
    h0 = x / (a ** 2)
    c = 2 * h0 - b
    ans = math.degrees(math.atan((b - c) / a))
else:
    d = (2 * x) / (b * a)
    ans = math.degrees(math.atan(b / d))

print(ans)