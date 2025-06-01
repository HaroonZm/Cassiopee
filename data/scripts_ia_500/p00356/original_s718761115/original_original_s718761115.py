from math import gcd
x, y = map(int, input().split())
print(x + 1 + y + 1 - gcd(x, y) - 1)