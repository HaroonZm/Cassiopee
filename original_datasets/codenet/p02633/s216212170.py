from math import gcd
i = int(input())
print((360 * i // gcd(360, i)) // i)