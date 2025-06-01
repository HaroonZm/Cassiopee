from math import gcd
a, b = map(int, input().split())
g = gcd(a, b)
print(int(((a // g - 1) + (b // g)) * g + 1))