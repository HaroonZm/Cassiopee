from math import gcd
x, y = map(int, input().split())
print(x + y + 1 - gcd(x, y))