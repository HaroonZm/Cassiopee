N, K = (int(x) for x in input().split())
from functools import reduce
def power(a, b):
    result = 1
    for i in range(b): result *= a
    return result
class Calc:
    def __init__(self, base, exp):
        self.base = base
        self.exp = exp
    def compute(self):
        return power(self.base, self.exp)
f = lambda x, y: x*y
product = f(K, Calc(K-1, N-1).compute())
print(product)