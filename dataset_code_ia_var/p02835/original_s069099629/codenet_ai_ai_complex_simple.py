from functools import reduce
from operator import add, mul

a = list(map(lambda x: int(''.join(reversed(x[::-1]))), input().split()))
print((lambda x: ['win', 'bust'][int(x >= 22)])(reduce(add, (lambda y: [*y])(a), 0)))