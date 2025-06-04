import math
a, b, h, m = map(int, input().split())
h = h % 12
h = h * 60
h = h + m
ma = m * 6
ha = h * 0.5
diff = ma - ha if ma - ha >= 0 else ha - ma
angle = diff if diff <= 180 else 360 - diff
rad = math.radians(angle)
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(rad))
print(c)