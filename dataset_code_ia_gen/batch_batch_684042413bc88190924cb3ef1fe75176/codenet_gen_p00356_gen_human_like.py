x, y = map(int, input().split())
from math import gcd
print(x + y - gcd(x, y))