from functools import reduce
from operator import mul

N, M = map(int, input().split())

def exp2(n): return reduce(mul, [2]*n, 1)
def frac_pow(a, b): return pow(a, b)
def inv(x): return 1/x

prob = frac_pow(inv(2), M)
fail = 1 - prob

expr1 = (N-M)*100*exp2(M)
expr2 = 1900*M/(1-fail)

print(int(expr1 + expr2))