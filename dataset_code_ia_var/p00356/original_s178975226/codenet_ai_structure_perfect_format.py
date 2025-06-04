import math

x, y = map(int, input().split())
result = x + y - math.gcd(x, y) + 1
print(result)