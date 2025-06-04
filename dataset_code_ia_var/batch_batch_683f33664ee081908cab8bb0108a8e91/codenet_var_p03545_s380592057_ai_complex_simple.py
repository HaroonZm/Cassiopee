from functools import reduce
from itertools import product

A = input()
indices = range(len(A)-1)
ops = [('+', '-')]
combos = list(product(*ops*len(indices)))
exprs = (''.join(reduce(lambda x, y: x + A[y[0]+1] + y[1], enumerate(combo), A[0]))
         for combo in combos)
res = next(filter(lambda s: eval(s) == 7, exprs))
print(f"{res}=7")