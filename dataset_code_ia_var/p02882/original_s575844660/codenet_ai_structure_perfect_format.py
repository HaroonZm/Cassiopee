import math

a, b, x = map(int, input().split())

y = x / a

if y <= (a * b) / 2:
    angle = 90 - math.degrees(math.atan((2 * y) / pow(b, 2)))
    print(angle)
else:
    y = a * b - y
    angle = math.degrees(math.atan((2 * y) / pow(a, 2)))
    print(angle)