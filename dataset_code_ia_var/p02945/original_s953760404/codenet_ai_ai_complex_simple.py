from functools import reduce
from operator import add, sub, mul

# Obscure décomposition et traitement
*A, = map(int, input().split())
op_fns = [add, sub, mul]
combinations = [fn(A[0], A[1]) for fn in op_fns]
print(reduce(lambda x, y: (x > y) * x + (y >= x) * y, combinations))