from math import gcd

x, y = map(int, input().split())
result = x + 1 + y + 1 - gcd(x, y) - 1
print(result)