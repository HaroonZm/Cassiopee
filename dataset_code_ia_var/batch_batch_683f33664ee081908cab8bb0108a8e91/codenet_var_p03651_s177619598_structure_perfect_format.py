from fractions import *
_, k, *a = map(int, open(0).read().split())
g = a[0]
for i in a:
    g = gcd(g, i)
if k > max(a) or k % g > 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")