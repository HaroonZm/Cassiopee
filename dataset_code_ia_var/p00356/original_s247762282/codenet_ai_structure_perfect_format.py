import math

a, b = map(int, input().split())
g = math.gcd(a, b)
a1 = a / g
b1 = b / g
result = int((a1 - 1 + b1) * g + 1)
print(result)