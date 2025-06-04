from functools import reduce
from operator import add

S, T = map(lambda x: x.strip(), [input(), input()])
X = reduce(add, map(lambda pair: int(pair[0] == pair[1]), zip(S, T, '   '))) if len(S) >= 3 and len(T) >= 3 else 0
print(X)