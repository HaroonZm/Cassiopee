from itertools import product
from functools import reduce

S = list(map(int, [input(), input(), input(), input()]))
X = S.pop()
possible = (range(S[0]+1), range(S[1]+1), range(S[2]+1))
vals = (500, 100, 50)

print(sum([1 for q in product(*possible) if reduce(lambda x, y: x+y, map(lambda x, y: x*y, q, vals)) == X]))