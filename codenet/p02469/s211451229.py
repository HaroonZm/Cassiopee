n = int(input())
a = [int(i) for i in input().split()]
import math
lcm = a[0]
for i in a[1:]:
    lcm = i * lcm // math.gcd(lcm, i)
print(lcm)