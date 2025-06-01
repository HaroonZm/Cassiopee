import math
n, m, r = map(int, input().split())
a = r - n * m
def combination(p, q):
    if q < 0 or p < q:
        return 0
    return math.factorial(p) // math.factorial(q) // math.factorial(p - q)
if a < 0:
    print(0)
else:
    print(int(combination(a + n - 1, a)))