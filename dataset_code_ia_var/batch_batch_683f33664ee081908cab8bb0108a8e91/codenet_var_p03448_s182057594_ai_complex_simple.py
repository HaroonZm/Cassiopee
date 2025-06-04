from itertools import product
from functools import reduce
from operator import add

inputs = list(map(int, [input(), input(), input(), input()]))
combinations = list(product(range(inputs[0]+1), range(inputs[1]+1), range(inputs[2]+1)))
deltas = map(lambda t: 500*t[0] + 100*t[1] + 50*t[2] - inputs[3], combinations)
matches = map(lambda d: 1 if d == 0 else 0, deltas)
ans = reduce(add, matches, 0)
print(ans)