import math
x, y = list(map(int, input().split()))
print(x + y - math.gcd(x, y) + 1)