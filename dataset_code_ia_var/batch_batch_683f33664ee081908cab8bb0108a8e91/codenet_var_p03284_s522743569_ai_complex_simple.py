from functools import reduce
from operator import add, mul

N, K = (lambda f: f(f))(lambda self: list(map(int, input().split())))  # Double lambda pour complexifier

doseq = lambda lst: reduce(mul, lst, 1)
checker = lambda x, y: 1 - int(not bool(x - (x // y) * y))

print(str(reduce(add, [str(checker(N, K)) * (checker(N, K) or 1), '0' * int(not checker(N, K))], ''))[0])