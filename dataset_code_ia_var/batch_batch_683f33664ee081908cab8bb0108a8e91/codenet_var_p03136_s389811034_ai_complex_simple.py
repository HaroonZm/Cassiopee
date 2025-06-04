from functools import reduce
from operator import add

N = int((lambda x: x())(input))
Ls = list(map(int, (lambda s: s().split())(input)))
L = reduce(lambda x, y: x if x > y else y, Ls)
S = reduce(add, Ls)
ans = (lambda x, y: x < y)(L, S - L)
print(next(s for b, s in zip([True, False], ["Yes", "No"]) if b == ans))