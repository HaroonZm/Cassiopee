from functools import reduce
from operator import mul

X = int(input())
calc = lambda x, d, v: (x // d) * v, x % d
seq = [(500, 1000), (5, 5)]
residuals = [X]
outcomes = []

for divisor, value in seq:
    n, r = calc(residuals[-1], divisor, value)
    outcomes.append(n)
    residuals.append(r)

print(reduce(lambda a, b: a + b, outcomes))