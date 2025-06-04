import math

x, y = list(map(int, input().split()))
gc = math.gcd(x, y)
print(x + y - gc + 1)