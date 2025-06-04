from functools import reduce

na = list(map(int, input().split()))
N, X = na[0], na[1]
x = list(map(int, input().split()))
y = [abs(v - X) for v in x]

def _gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a

res = y[0]
for v in y[1:]:
    res = _gcd(res, v)

print(res)