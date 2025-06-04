from functools import reduce
import operator

n, k = map(int, input().split())

res = (lambda x: reduce(operator.xor, [0, int(bool(x % k))]))
print(res(n))