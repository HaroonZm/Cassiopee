from functools import reduce
from operator import add

S, T = (lambda: (input(), input()))()

indices = map(lambda x: x, range(3))
matches = map(lambda i: 1 if S[i] == T[i] else 0, indices)
result = reduce(add, matches, 0)

print(result)